---
article_id: 37093881771159
category: Administração de Pessoal
content_hash: 304584b79fae0c702bd4cdb1966d0fbc98927818790dca6bd62fe667d424afaf
fetched_at: '2026-06-28T22:47:01.106119+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Novo Cálculo IRRF - LEI 15.270
type: support-article
updated_at: '2026-06-01T13:47:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37093881771159-RH-RM-FOP-Novo-C%C3%A1lculo-IRRF-LEI-15-270
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37093876210327) Tempo aproximado para leitura: **00:04:15 min**

**Dúvida**  
Quais versões posso utilizar e como parametrizar o sistema e para atender a nova Lei 1.5270 referente ao cálculo do IRRF?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir da 12.1.2502  
  
**Solução**  
Foi sancionada e publicada no Diário Oficial da União a [Lei nº 15.270, de 26 de novembro de 2025](https://legislacao.presidencia.gov.br/atos/?tipo=LEI&numero=15270&ano=2025&ato=ab5k3aU9UNZpWTab7), que promove uma ampla reestruturação no **Imposto de Renda da Pessoa Física (IRPF).** As novas regras começam a produzir efeitos a partir de 1º de janeiro de 2026 e têm como objetivo corrigir a tabela do imposto, reduzir a carga tributária de trabalhadores de baixa renda e instituir novos mecanismos de tributação sobre rendimentos elevados.

**Veja mais detalhes em:**  
- [**Nova Lei do IRPF: Redução para Baixa Renda e Tributação Mínima para Altas Rendas**](https://www.totvs.com/blog/fiscal-clientes/nova-lei-do-irpf-reducao-para-baixa-renda-e-tributacao-minima-para-altas-rendas/)  
- [**Orientações Consultoria de Segmentos - Novo Cálculo do IRRF**](https://tdn.totvs.com/pages/releaseview.action?pageId=1019343450)

A principal novidade para a maioria dos contribuintes é a introdução de uma **redução no valor do imposto devido nas apurações mensais e anuais**, beneficiando as faixas de menor rendimento.

* **Redução Mensal (a partir de janeiro de 2026)**  
  A lei estabelece uma nova tabela de redução do IRPF que incide sobre os rendimentos sujeitos ao ajuste mensal.

|  |  |
| --- | --- |
| **LIMITE RENDIMENTO** | **REGRA** |
| Até R$5000,00 mensais | IRRF zerado |
| Entre R$5000,01 e R$7350,00 mensais | Aplicar redutor (conforme fórmula legal) no valor do IRRF |
| Acima de R$7350,00 mensais | IRRF sem redutor |

* **Redução Anual (a partir do ano-calendário de 2026, exercício de 2027)**  
  Além da redução mensal, a lei prevê uma redução anual complementar, aplicada no momento da declaração, ampliando o benefício para quem se enquadra nas faixas mais baixas. Além disso, o valor da dedução anual simplificada foi ajustado, passando de R$ 16.754,34 (até 2025) para R$ 17.640,00 (a partir do ano-calendário de 2026).

**Versões e Documentações**

Realizamos a liberação das alterações para atender a nova Lei 15270. Abaixo os Patches que contemplam as mudanças e devida documentação:

12.1.2502.251  
12.1.2506.209  
12.1.2510.137  
e superiores

⚠️ [Como calcular a Isenção do Imposto de Renda para quem ganha até 5.000,00 e redução gradual até 7.350,00 - LEI 15.270/2025](https://tdn.totvs.com.br/pages/releaseview.action?pageId=1021212238)

**Atenção!!** Pontos **importantes** (detalhados na documentação acima):

**- Não** é necessário executar o **RM.Atualizador.exe**;  
- A tabela original de IRRF de **finalidade "****2 - IRRF****"** continua existindo, ou seja, **seus valores não serão alterados**. Para 2026, pode-se **atualizar a vigência** da tabela atual.   
- Deve-se criar uma **nova Tabela de Cálculo** de **finalidade "****6 - IRRF\_REDUÇÃO****"** onde deverão ser informados os valores para o cálculo da redução com a **vigência** a partir de 01/01/2026;  
Para que a finalidade 6 apareça para cadastro, é necessário **executar o recálculo da folha de ao menos 1 funcionário**.

**Calculo Pensão Nova Tabela IRRF Redução**

 12.1.2410.319  
 12.1.2502.229  
 12.1.2506.179  
 12.1.2510.112  
 e superiores

⚠️ [Cálculo Pensão Nova Tabela IRRF Redução](https://tdn.totvs.com/pages/releaseview.action?pageId=1031534137)

🖥️ **Evento Webinar**

Veja abaixo a gravação do evento TOTVS Responde realizado sobre o tema:

* [Espaço Legislação | Reforma da Tributação sobre a Renda | TOTVS RH e Fiscal Linha RM](https://www.youtube.com/watch?v=ftxO-HVPjVk)

**Lucros e Dividendos na Folha de Pagamento**

Conforme análise da equipe de consultoria de segmentos da TOTVS,:

*"Os lucros e dividendos possuem **natureza eminentemente societária**, decorrente da participação do sócio ou acionista no capital social da empresa, não estando vinculados à prestação de serviços. Nos termos da legislação trabalhista, a remuneração do empregado está definida no **art. 457 da Consolidação das Leis do Trabalho (CLT)**, que restringe sua composição às parcelas pagas como contraprestação pelo trabalho. Os dividendos, por sua vez, não se enquadram nesse conceito, pois resultam da apuração do lucro e de deliberação societária, inexistindo vínculo com a força de trabalho. [...]*  
  
*Dessa forma, entende-se que os **lucros e dividendos não integram a folha de pagamento**, não gerando incidência de INSS, FGTS ou demais encargos trabalhistas e previdenciários. [...]*  
  
*Mesmo após a alteração normativa que instituiu a tributação dos lucros e dividendos pelo Imposto de Renda, permanece íntegro o entendimento legal de que tais valores não possuem natureza salarial, não integram a folha de pagamento e não sofrem incidência de encargos trabalhistas ou previdenciários, desde que observados os requisitos legais, contábeis e societários que legitimam sua distribuição. "*

Veja mais detalhes sobre o assunto no item 5 do documento abaixo:

- [**Orientações Consultoria de Segmentos - Novo Cálculo do IRRF**](https://tdn.totvs.com/pages/releaseview.action?pageId=1019343450)

🖥️ **How To**

Acompanhe nossos [informativos](https://informa.totvs.com/rh/) e fique por dentro das novidades!
