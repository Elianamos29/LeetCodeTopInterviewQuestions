class Solution:
    def simplifyPath(self, path: str) -> str:
        canonical_path = []
        elems = []

        p = path.split("/")
        for e in p:
            if e:
                elems.append(e)
        
        for s in elems:
            if s == '.':
                continue
            elif s == '..':
                if canonical_path:
                    canonical_path.pop()
            else:
                canonical_path.append(s)

        return "/" + "/".join(canonical_path)

if __name__ == '__main__':
    s = Solution()
    print(s.simplifyPath("/home/"))
    print(s.simplifyPath("/../"))
    print(s.simplifyPath("/home//foo/"))
    print(s.simplifyPath("/a/./b/../../c/"))
    print(s.simplifyPath("/a/../../b/../c//.//"))
    print(s.simplifyPath("/a//b////c/d//././/.."))
    print(s.simplifyPath("/home/user/Documents/../Pictures"))
    print(s.simplifyPath("/abc/..."))
    print(s.simplifyPath("/..hidden"))
    print(s.simplifyPath("/hello../world"))