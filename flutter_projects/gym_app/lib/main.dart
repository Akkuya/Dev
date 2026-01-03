import 'package:flutter/material.dart';
import 'package:gym_app/ui/home.dart';
import 'package:gym_app/ui/workouts.dart';
import 'package:gym_app/ui/current.dart';
import 'package:gym_app/ui/analytics.dart';

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

void main() {
  runApp(const MyApp());
}

class _MyAppState extends State<MyApp> {
  int _currentIndex = 0;

  final List<Widget> _screens = const [
    HomeScreen(),
    WorkoutsScreen(),
    AnalyticsScreen(),
    CurrentScreen(),
  ];

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(useMaterial3: true),
      home: Scaffold(
        appBar: AppBar(
          title: Text(
            ['Home', 'Workouts', 'Current', 'Analytics'][_currentIndex],
            style: const TextStyle(fontSize: 28, fontWeight: FontWeight.bold),
          ),
        ),

        body: IndexedStack(index: _currentIndex, children: _screens),

        bottomNavigationBar: BottomNavigationBar(
          currentIndex: _currentIndex,
          type: BottomNavigationBarType.fixed,
          onTap: (index) {
            setState(() => _currentIndex = index);
          },
          items: const [
            BottomNavigationBarItem(icon: Icon(Icons.home), label: 'Home'),
            BottomNavigationBarItem(
              icon: Icon(Icons.fitness_center),
              label: 'Workouts',
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.play_arrow),
              label: 'Train',
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.bar_chart),
              label: 'Analytics',
            ),
          ],
        ),
      ),
    );
  }
}
