---
article_id: 360015780592
category: RH - 13º salário
content_hash: 746651bb3217b82abae589e13abd0d2747f0176c0e1d3a9ce7998e648c252d4f
fetched_at: '2026-06-28T22:44:00.502013+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Como analisar médias no calculo de 13º Salário
type: support-article
updated_at: '2025-08-20T14:13:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015780592-RH-Linha-Protheus-GPE-Como-analisar-m%C3%A9dias-no-calculo-de-13%C2%BA-Sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18898048630679) Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como analisar médias no cálculo de 13º Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A princípio, verifique o **DEM\_MED** que é o relatório de médias pelo cálculo em **Atualizações > Lançamentos > Por funcionário GPEA580**

Selecione o funcionário e clique em **Visualizar**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18928939068183)

Altere o roteiro de **FOL** para o roteiro **131** ou **132** dependendo de qual tenha calculado e clique em **Outras Ações > Médias**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18928906204695)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18928939093911)

O cálculo da primeira parcela segue a mesma linha de raciocino da segunda parcela.  
Diferença: Em vez de trazer a média de pagamento integral ele irá levar apenas 50% do valor.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18928906222999)

**Verifique particularidades pelo sindicato.**O sistema verifica cadastro da verba que incide médias como prioridade;  
Se no **cadastro da verba** estiver com **"S"** para médias, o sistema respeita o **cadastro de sindicatos;**Se estiver com conteúdo **"0"** ou **vazio,** o sistema fará a divisão conforme CLT, respeitando a regra estabelecida no **Mnemônico P\_MEDDIREN**  
  
**Exemplo 1:**  
Cadastro da verba = S  
Cadastro de sindicatos = 0  
P\_MEDDIREN = N  
  
Cálculo:  
Total Médias (Médias recebidas durante o ano) / Avos de Direito = Média  
Média / 12 \* Avos de Direito = Valor média **pagamento**.  
  
**Exemplo 2:**  
Cadastro da verba = S  
Cadastro de sindicatos = 0  
P\_MEDDIREN = S

Cálculo:  
Total das médias / Avos de direito = Valor média **pagamento**.

**Exemplo 3:**  
Cadastro da verba = S  
Cadastro de sindicatos = 0  
P\_MEDDIREN = M

* Funcionário com contrato por tempo determinado e duração igual ou inferior a um ano.

Cálculo:   
Total das médias (Somatório das verbas com incidência para média) / Meses considerados para média\* = Valor média PAGAMENTO.

**Exemplo 4:**  
Cadastro da verba = S  
Cadastro de sindicatos = 0  
P\_MEDDIREN = M

* Funcionário com contrato por tempo determinado e duração superior a um ano.

Cálculo:

Total Médias (Somatório das verbas com incidência para média) / Meses considerados para média\* = Média

Média / 12 \* Avos de Direito = Valor Média PAGAMENTO.

**Exemplo 5:**  
Cadastro da verba = S  
Cadastro de sindicatos = 6  
P\_MEDDIREN = N

Cálculo:  
O sistema vai buscar os 6 últimos meses (MV\_REFMED = .T. ele abre a tela de parâmetros para decidir a partir de qual mês se for versão 11, a partir da 12 a pergunta está nos parâmetros do cálculo mesmo)  
Total Médias (últimos 6 meses) / Avos de Direito = Média  
Média / 12 \* Avos de Direito = Valor média **pagamento**.  
  
**Exemplo 6:**Cadastro da verba = S  
Cadastro de sindicatos = 6  
P\_MEDDIREN = S

Cálculo:  
O sistema irá buscar os 6 últimos meses (MV\_REFMED = .T. ele abre a tela de parâmetros para decidir a partir de qual mês se for versão 11, a partir da 12 a pergunta está nos parâmetros do cálculo mesmo)  
Total Médias (últimos 6 meses) / Avos de Direito = Valor média **pagamento**.  
  
Base: <https://tdn.totvs.com/pages/releaseview.action?pageId=224112471>

**Saiba Mais**  
O conteúdo também está disponível no *link* a seguir: [Roteiro de Análise 13º Salário - Primeira e Segunda Parcela](http://tdn.totvs.com/pages/viewpage.action?pageId=219682468)

[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
Essas **documentações** também podem ser acessadas através da **Carolina**, veja como acessar a assistente virtual, via **Protheus** ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>
