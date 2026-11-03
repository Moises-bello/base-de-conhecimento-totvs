---
article_id: 1500004356402
category: Gestão de Frotas
content_hash: af2d579687bc42bf5565ff9f604aeb8b94c96b77c5f199dcd748f9dc93cf186b
fetched_at: '2026-06-28T22:42:39.599928+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Tela Seleção de Filiais Conciliação Manual
  de Posto Interno - MNTA670
type: support-article
updated_at: '2021-08-30T20:06:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004356402-Manufatura-Linha-Protheus-MNT-Tela-Sele%C3%A7%C3%A3o-de-Filiais-Concilia%C3%A7%C3%A3o-Manual-de-Posto-Interno-MNTA670
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Porque aparece a tela de **Seleção de Filiais** quando concilia abastecimentos na rotina **Conciliação Manual de Posto Interno - MNTA670**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas – Versão 12  
  
**Solução**A tela irá aparecer para **Abastecimentos - TQN** onde o **Posto Interno** esteja cadastrado em mais de uma filial com o mesmo **Código de Tanque - TQI\_TANQUE**.  
O motivo da seleção é pelo fato do Sistema não saber de qual **Almoxarifado** - **Tanque** o usuário deseja debitar o saldo abastecido visto que a rotina poderá trazer registros de todas as filiais por meio da pergunta **Todas as Filiais?** igual a **Sim**.  
Os procedimentos para que a apresente a tela de **Seleção de Filiais**, são:

1. Configure os parâmetros:   
   **MV\_ESTHOME - Indica o momento que o estoque será debitado.** igual a **C - Conciliação  
   MV\_NGMNTES - Integração Manutenção - MNT com Estoque - EST** igual a **S - Sim  
   MV\_ESTNEG - Identifica se o Sistema permitirá que os saldos em estoque dos produtos fique negativo através de movimentação** igual a **N - Não  
   MV\_NGMNTFR - Indica se a empresa ira utilizar o Gestão de Frota** igual a **S - Sim.**
2. Acesse o módulo de **Estoque/Custos - SIGAEST**;
3. Inclua um **Fornecedor - MATA020**;
4. Inclua um **Produto - MATA010**;
5. Inclua um **Saldo Inicial para esse Produto - MATA220**.
6. Acesse o módulo de **Manutenção de Ativos e Gestão de Frotas - SIGAMNT**;
7. Inclua um **Tipo de Combustível - MNTA640**;
8. Inclua **Posto do tipo Interno - MNTA610**;
9. Informe **Tanques/Bombas - MNTA615**;
10. Os passos acima devem possuir registros em pelo menos duas filiais.
11. Inclua um **Veículo - MNTA084** do tipo **Frota não Integrada ao TMS**, informando **Placa - T9\_PLACA**, **Contador - T9\_POSCONT** e **Tanque - TT8\_TIPO**;
12. Realize um**Abastecimento Manual - MNTA655**;
13. Acesse a rotina de **Conc. Manual Posto Interno - MNTA670**, informando os parâmetros conforme registros incluídos anteriormente;
14. Selecione a folha do abastecimento incluída anteriormente e verifique que a tela de **Seleção de Filiais** é apresentada.
