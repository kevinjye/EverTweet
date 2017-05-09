if [ -d "$testcases" ]; then
  for f in testcases/*.py;
      do python "$f";
  done
fi
