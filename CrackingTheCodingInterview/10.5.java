int search(String[] strings, String str, int first, int last) {
    if(first > last) {
        return -1;
    }
    
    int mid = (last + first) / 2;
    
    /* if 'mid' is empty, find a string that is closest to 'mid' */
    if(strings[mid].isEmpty()) {
        int left = mid - 1;
        int right = mid + 1;
        while (true) {
            if(left < first && right > last) {
                return -1;
            } else if (right <= last && !strings[right].isEmpty()) {
                mid = right;
                break;
            } else if (left >= first && !strings[left].isEmpty()) {
                mid = left;
                break;
            }
            right++;
            left--; 
        }
    }

    /* check a string and do recursion if necessary */ 
    if (str.equals(strings[mid])) {
        return mid;
    } else if (strings[mid].compareTo(str) < 0) {
        return search(strings, str, mid + 1, last);
    } else {
        return search(strings, str, first, mid - 1);
    }
}

int search(String[] strings, String str) {
    if (strings == null || str == null || str == "") {
        return -1;
    }

    return search(strings, str, 0, strings.length - 1);
}