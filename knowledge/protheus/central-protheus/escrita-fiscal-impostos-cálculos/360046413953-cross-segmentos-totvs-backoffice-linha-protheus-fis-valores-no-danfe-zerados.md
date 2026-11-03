---
article_id: 360046413953
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 11788e07459fab5e63d64cc53b040157bd7c8a0716faba80398d39ba0608d8ff
fetched_at: '2026-06-28T22:39:30.472068+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: ' CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Valores no DANFE
  Zerados'
type: support-article
updated_at: '2021-07-29T13:19:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046413953--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Valores-no-DANFE-Zerados
---

**Dúvida**Qual a configuração no sistema para que os campos Quantidade, Valor Unitário, Valor Total, Base de ICMS e Base de IPI sejam gravados zerados no Danfe?  
  
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
Neste caso pode ser gerado uma nota de AJUSTE onde os campos quantidade, valor unitário, valor total, base de ICMS e base de IPI devem sair zerados no Danfe.  
  
No TES deixe o campo F4\_AJUSTE com SIM.  
  
Como o Sistema não tem um tratamento especifico para notas de Ajuste, gere uma nota de complemento de ICMS.  
  
O TES utilizado não deve gerar nenhuma informação dos impostos, mas deve ter uma fórmula no campo F4\_FORMULA para que as tabelas Livros Fiscais (SF3) e Livros Fiscais por Item de NF (SFT) sejam preenchidas e a nota transmitida.  
  
Segue exemplo de como deve ficar o TES:  
  
Configuração necessário no TES:  
  
Credita ICMS =Sim   
Calcula ICMS = Não  
Gera Duplicata = Sim  
Livro Fiscal= Outros  
Agrega Solidário = Não  
Fórmula = Amarrar uma fórmula com conteúdo texto = Complemento, para que o Sistema não destaque o ICMS normal nos livros.  
  
Com isso a nota é transmitida e os valores no Danfe são zerados. Mas é necessário informar um valor para os campos Valor Unitário e Valor Total.  
  
No valor unitário e total é o valor do crédito no campo de NFORI pode preencher com qualquer texto que faça sentido EX: "NFCREDITO"  
  
Fazer a amarração do código da tabela 5.3 no TES em lançamentos da apuração no campo CC7\_CODLAN e informar um código de reflexo no campo CC7\_CODREF que dever cadastrado na rotina FISA072.  
  
Segue abaixo o exemplo do código de reflexo:

Na rotina de Código de Ajuste de Reflexo - Apuração de ICMS, preencher os campos abaixo:

Código = Definido pelo cliente  
Prioridade = 0  
Descrição = Definido pelo cliente  
Base P/ Calc = 1-Base ICMS  
Alíquota = 1-Alq ICMS  
Vl. Aliquota = 0,00  
Vaor = 3-Merc  
Vl Reg 197 = Branco  
Tr Genérico = Branco

![](https://totvssuporte.zendesk.com/attachments/token/B9Mter57Okng8y5Y0ALXEixvr/?name=inline-939420997.png)​
