if [ -d "testcases" ]; then
  cd testcases
  for f in *.py;
      do python $f;
  done
fi
