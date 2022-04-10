# Medicar
## Cadastrar médico
Deve ser possível cadastrar os médicos que podem atender na clínica fornecendo as seguintes informações:

-Nome: Nome do médico (obrigatório)
-CRM: Número do médico no conselho regional de medicina (obrigatório)
-E-mail: Endereço de e-mail do médico (opcional)

#### Restrições:
Não deve ser possível cadastrar médico com um CRM que outro médico já utilize

## Criar agenda para médico
Deve ser possível criar uma agenda para o médico em um dia específico fornecendo as seguintes informações:

- Médico: Médico que será alocado (obrigatório)
- Dia: Data de alocação do médico (obrigatório)
- Horários: Lista de horários na qual o médico deverá ser alocado para o dia especificado (obrigatório)
#### Restrições:
- Não deve ser possível criar mais de uma agenda para um médico em um mesmo dia
- Não deve ser possível criar uma agenda para um médico em um dia passado

### Listar Agendas dos Medicos - GET
<pre>
	<code>
		api/scheduleMedic
	</code>
</pre>
- Retorno:
<pre>
	<code>
	{
		"ScheduleId": 1,
		"MedicId": 1,
		"Day": "2022-04-24",
		"Hours": "16:36"
	}
	</code>
</pre>

### Criar Agenda dos Medicos - POST

<pre>
	<code>
		api/scheduleMedic
	</code>
</pre>
<pre>
	<code>
	{
		"MedicId":"1",
		"Day": "2022-04-27",
		"Hours": "9:00;10:00;11:00"
	}
	</code>
</pre>

### Listar as consultas - GET

<pre>
	<code>
		/api/consult
	</code>
</pre>

-Retorno

<pre>
	<code>
	{
		"ConsultId": 3,
		"DayConsult": "2022-04-09",
		"Hour": "10:00",
		"SchedulingDate": "2022-04-10T15:14:36.769470Z",
		"ScheduleId": 1
	},
	{
		"ConsultId": 6,
		"DayConsult": "2022-04-24",
		"Hour": "13:00",
		"SchedulingDate": "2022-04-10T15:25:07.516763Z",
		"ScheduleId": 1
	}
	</code>
</pre>

### Criar Consulta - POST

<pre>
	<code>
		/api/consult
	</code>
</pre>

<pre>
	<code>
	{
		"ScheduleId": 1,
		"Hour": "16:36"
	}
	</code>
</pre>

### Deletar Consulta - DELETE

<pre>
	<code>
		/api/consult/id
	</code>
</pre>

### Cadastrar Medico

<pre>
	<code>
		/api/medic
	</code>
</pre>

<pre>
	<code>
	{
		"MedicName":"Teste",
		"Crm": "7412",
		"Email": "teste@gmail.com"
	}
	</code>
</pre>

PS: Antes de executar a API alterar credenciais do banco e no terminal do VS Code : python manage.py migrate MedicarApp
