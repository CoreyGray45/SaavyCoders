name="Lacey Raye Gray"
echo "How are you today, $name?"
sleep 2
echo "You look beautiful today"
question1="Is it your birthday?"
echo $question1
read answer1

if [ "$answer1" == "yes" ]; then
  echo "Happy Birthday!"
else
  echo "Whose birthday is today?"
fi