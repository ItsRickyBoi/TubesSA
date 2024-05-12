function findPalindrome() {
    let inputString = document.getElementById('inputString').value;
    if (/[\d]/.test(inputString)) {
        alert("Input wrong, try again. Only alphabetic strings are allowed.");
        return;
    }

    clearCanvas('palindromeCanvasBF');
    clearCanvas('palindromeCanvasDP');
    let resultBF = findLongestPalindromeBF(inputString);
    let resultDP = findLongestPalindromeDP(inputString);
    document.getElementById('resultBF').innerHTML = `Brute Force - Longest Palindrome: ${resultBF}`;
    document.getElementById('resultDP').innerHTML = `Dynamic Programming - Longest Palindrome: ${resultDP}`;
}

function clearCanvas(canvasId) {
    const canvas = document.getElementById(canvasId);
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function findLongestPalindromeBF(s) {
    const canvas = document.getElementById('palindromeCanvasBF');
    const ctx = canvas.getContext('2d');
    const charWidth = canvas.width / s.length;

    let maxLength = 0, start = 0;

    for (let i = 0; i < s.length; i++) {
        for (let j = i; j < s.length; j++) {
            if (isPalindrome(s, i, j)) {
                drawRectangle(ctx, i, j, charWidth, 'lightcoral', s.substring(i, j+1));
                if (j - i + 1 > maxLength) {
                    maxLength = j - i + 1;
                    start = i;
                }
            }
        }
    }

    drawRectangle(ctx, start, start + maxLength - 1, charWidth, 'lightblue', s.substring(start, start + maxLength));
    return s.substring(start, start + maxLength);
}

function findLongestPalindromeDP(s) {
    const canvas = document.getElementById('palindromeCanvasDP');
    const ctx = canvas.getContext('2d');
    const charWidth = canvas.width / s.length;
    let n = s.length;
    let dp = Array.from(Array(n), () => new Array(n).fill(false));
    let maxLength = 1, start = 0;

    // All single characters are palindromes
    for (let i = 0; i < n; i++) {
        dp[i][i] = true;
        drawRectangle(ctx, i, i, charWidth, 'lightcoral', s[i]);
    }

    // Check for two-character palindromes
    for (let i = 0; i < n - 1; i++) {
        if (s[i] === s[i + 1]) {
            dp[i][i + 1] = true;
            drawRectangle(ctx, i, i + 1, charWidth, 'lightcoral', s.substring(i, i+2));
            start = i;
            maxLength = 2;
        }
    }

    // Check for palindromes longer than 2
    for (let len = 3; len <= n; len++) {
        for (let i = 0; i < n - len + 1; i++) {
            let j = i + len - 1;
            if (s[i] === s[j] && dp[i + 1][j - 1]) {
                dp[i][j] = true;
                drawRectangle(ctx, i, j, charWidth, 'lightcoral', s.substring(i, j+1));
                if (len > maxLength) {
                    start = i;
                    maxLength = len;
                }
            }
        }
    }

    drawRectangle(ctx, start, start + maxLength - 1, charWidth, 'lightblue', s.substring(start, start + maxLength));
    return s.substring(start, start + maxLength);
}

function drawRectangle(ctx, start, end, charWidth, color, text) {
    ctx.fillStyle = color;
    ctx.fillRect(start * charWidth, 0, (end - start + 1) * charWidth, 50);
    ctx.strokeStyle = 'black';
    ctx.strokeRect(start * charWidth, 0, (end - start + 1) * charWidth, 50);
    ctx.fillStyle = 'black';
    ctx.fillText(text, start * charWidth + 5, 25, (end - start + 1) * charWidth);
}

function isPalindrome(s, left, right) {
    while (left < right) {
        if (s[left] !== s[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
