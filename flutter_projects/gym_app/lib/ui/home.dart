import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,

      children: [
        Row(
          children: [
            Expanded(
              child: ElevatedButton(
                onPressed: () {},
                style: ElevatedButton.styleFrom(
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(16),
                  ),
                  padding: const EdgeInsets.symmetric(vertical: 100),
                ),
                child: const Text(
                  "Start Workout",
                  style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                ),
              ),
            ),
            const SizedBox(width: 16),
            Expanded(
              child: ElevatedButton(
                onPressed: () {},
                style: ElevatedButton.styleFrom(
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(16),
                  ),
                  padding: const EdgeInsets.symmetric(vertical: 100),
                ),
                child: const Text(
                  "Create Workout",
                  style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                ),
              ),
            ),
          ],
        ),
        const SizedBox(height: 10), // spacing between buttons and header
        Align(
          alignment: Alignment.centerLeft,
          child: Padding(
            padding: const EdgeInsets.symmetric(
              horizontal: 15,
            ), // adjust if needed
            child: const Text(
              "Recent",
              style: TextStyle(fontSize: 40, fontWeight: FontWeight.bold),
            ),
          ),
        ),
        const SizedBox(height: 10), // spacing between header and cards
        Column(
          children: [
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 15),
              child: _workoutCard(
                name: "Push Day",
                time: "Yesterday",
                volume: "12,500 kg",
                duration: "1h 15m",
              ),
            ),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 15),
              child: _workoutCard(
                name: "Pull Day",
                time: "2 days ago",
                volume: "10,300 kg",
                duration: "1h 05m",
              ),
            ),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 15),
              child: _workoutCard(
                name: "Leg Day",
                time: "3 days ago",
                volume: "15,800 kg",
                duration: "1h 30m",
              ),
            ),
          ],
        ),

        const SizedBox(height: 12),

        // --- VIEW ALL BUTTON ---
        Align(
          alignment: Alignment.center,
          child: TextButton(
            onPressed: () {},
            child: const Text("View All", style: TextStyle(fontSize: 16)),
          ),
        ),
      ],
    );
  }
}

Widget _workoutCard({
  required String name,
  required String time,
  required String volume,
  required String duration,
}) {
  return Card(
    margin: const EdgeInsets.only(bottom: 12),
    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
    elevation: 2,
    child: Padding(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Top row: name + time
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                name,
                style: const TextStyle(
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                ),
              ),
              Text(time, style: const TextStyle(color: Colors.grey)),
            ],
          ),
          const SizedBox(height: 8),

          // Bottom row: volume + duration
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [Text("Volume: $volume"), Text("Time: $duration")],
          ),
        ],
      ),
    ),
  );
}
