import 'package:flutter/material.dart';

class CurrentScreen extends StatelessWidget {
  const CurrentScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return const Center(
      child: Text(
        "Current",
        style: TextStyle(fontSize: 24),
      ),
    );
  }
}
