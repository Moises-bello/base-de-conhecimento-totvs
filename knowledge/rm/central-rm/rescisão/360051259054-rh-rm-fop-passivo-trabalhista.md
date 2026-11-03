---
article_id: 360051259054
category: Rescisão
content_hash: 0f18b27e6f60e5dfa60f6e72831a7924d4a11e93d54ee25d97b734f9aef3121a
fetched_at: '2026-06-28T22:46:55.297394+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: RH - RM - FOP - Passivo Trabalhista
type: support-article
updated_at: '2024-06-19T22:35:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051259054-RH-RM-FOP-Passivo-Trabalhista
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20639951264919)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Como gerar o relatório de passivo trabalhista?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Este processo permite emitir em relatório a provisão das principais verbas que deverão ser pagas aos funcionários na rescisão.  
  
1. Para realizar o processo do passivo trabalhista, acesse: **Rescisão | Passivo Trabalhista**:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4634504954647)  
  
2. Após acessar o menu, o usuário deverá informar a data de demissão. Caso a provisão seja dispensa sem justa causa, deverá informar se o aviso é indenizado ou não.  
  
3. Logo, informe quais verbas terão incidência de FGTS.  
  
4. Escolha as opções a serem realizadas na provisão do cálculo:

* Considera os 'Eventos Adicionais' definidos nos 'Parâmetros de Rescisão' para Base de Remuneração;
* Emissão do Passivo Trabalhista em Relatório;
* Desconsidera acréscimo de 10% na multa FGTS;
* Calcular desconto de INSS;
* Calcular Desconto de IRRF;
* Aviso Prévio indenizado abate 0,5 dia - parâmetro deve ser usado junto com **Considera Rescisão por comum acordo (Tipo V).**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080368974)  
  
5. Informe qual relatório será usado para geração. Caso deseje, poderá gerar o **FOPREL0002 - Relatório Passivo Trabalhista - Analítico**, que é o relatório comum, ou utilizar o relatório **FOPREL7072 - Relatório Passivo Trabalhista - Analítico - Subtotais**, que será gerado com subtotais de acordo com a quebra de seção informada.   
  
6. Após clicar em avançar, haverá a opção de usar parâmetros específicos por coligada, podendo informar a seleção de funcionários para os quais deseja fazer a provisão do Passivo Trabalhista.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080377374)  
  
Funcionalidade dos parâmetros:

* **Aviso Prévio indenizado abate 0,5 dia**: Quando marcado, o processo abate metade do dia para o cálculo do valor dos dias de aviso prévio de direito. Este parâmetro deve ser utilizado junto ao parâmetro **Considera Rescisão por comum acordo.**

**Parâmetro marcado:** Dias de Aviso: 17 Salário Base: R$1.500,00 Salário Dia: 1.500,00 / 30 = 50,00 Valor do Aviso Prévio: 16,5 \* 50,00 = R$825,00.  
  
**Parâmetro desmarcado:** Dias de Aviso: 17 Salário Base: R$1.500,00 Salário Dia: 1.500,00 / 30 = 50,00 Valor do Aviso Prévio: 17 \* 50,00 = R$850,00.

* **Considera Rescisão por comum acordo**: Quando marcado, o processo altera o percentual do valor pago para FGTS para 20% e não mais 40% (normal).

**Parâmetro marcado:** Saldo para Fins Rescisórios (R$5000,00) \* Multa (0,20) = R$1000,00

**Parâmetro desmarcado:** Saldo para Fins Rescisórios (R$5000,00) \* Multa (0,40) = R$2000,00

**Saiba mais :** [TDN - Passivo Trabalhista](https://tdn.totvs.com.br/display/public/LRM/Passivo+Trabalhista)  
[TDN - Consulta Movimento Passivo Trabalhista](https://tdn.totvs.com.br/display/public/LRM/Consulta+Movimento+Passivo+Trabalhista)
