---
content_hash: efd225b9787bd92eb6ee77192c03281fee6994b799d700e8f8a0f4b96bc46da0
fetched_at: '2026-06-29T00:10:03.173909+00:00'
page_id: '452719038'
product: rm
source: tdn-rm
title: Banco de Horas - Parametrizador
type: documentation
url: https://tdn.totvs.com/display/LRM/Banco+de+Horas+-+Parametrizador
version: 2
---

**Banco de Horas**   
**Localização : Automação de Ponto| Parametrizador| Sindicato| Etapa 12- Banco de horas**  
   
   
**Considera percentual para exibir no saldo do banco de horas**  
   
Este parâmetro tem por objetivo considerar o percentual de incidência das horas extras ao apurar o saldo de banco de horas. Caso marcado, será considerado o percentual de incidência da hora extra. Pré-Requisito: Os eventos de extras devem ter o parâmetro "Considera percentual de incidência" marcado. **O percentual será demonstrado nas funcionalidades abaixo:** Movimento | Banco de Horas por Dia: Créditos, Débitos e Saldos Movimento | Histórico do Saldo do Banco de Horas: Extra Anterior e Extra Atual Relatório do Espelho do Funcionário: Saldo do Período RM Portal | Saldo do Banco de Horas do Funcionário: Saldo Atual RM Portal | Espelho do Funcionário: Saldo Anterior e  Saldo Atual

**Exemplo:** Extra Faixa 1: 02:00 Evento: Hora Extra 50% Percentual: 1.5 Extra Faixa 2: 02:00 Evento: Hora Extra 100% Percentual: 2.0 Parâmetro marcado : Extra Atual: 07:00 (Considerando percentual) Parâmetro desmarcado : Extra Atual: 04:00 (Desconsiderando percentual)  
   
**Limite exec. por dia:** Permite criar um limite de jornada diária. **Limite exec. por semana:** Permite criar um limite de jornada semana. **Limite exec. por período:** Permite criar um limite de jornada por período.   
**Considera percentual de incidência para o limite do banco de horas:** Habilitando este parâmetro o sistema irá calcular percentual de incidência sobre o limite de horas da jornada estipulado na parametrização. 

**Exemplo:**  
Considerando limite de extra diário : 02:00h Funcionário realiza 1:46h de extra reduzida. Aplicando o percentual o valor de extras seriam 02:01h. Cálculo:  
1:46h => 106 minutos  
106 \* 1,1429 (percentual noturno) = 121 121 minutos => 02:01h  
Neste caso, após a aplicação do percentual o valor das horas superará o limite diário e com isso, a ocorrência irá alterar de faixa ou alterar a atitude (de acordo com a parametrização). **Observação:** Este cálculo não é exclusivo a ocorrência de extra mas sim a toda jornada. Isso dependerá da parametrização de limites no banco de horas.

**Considera Atitude do Evento** Este parâmetro tem por objetivo considerar a atitude que está informada no evento. A mesma encontra-se na aba Eventos - Informações Adicionais - Atitude a ser Considerada no Dia/Evento.

**Observação:** A alteração de atitude pelo menu de ocorrências coletadas ou modificação de ocorrências, não será considerada quando existir fórmula de lançamento para o banco de horas e estiver marcado o parâmetro "Considera Atitude do Evento".
