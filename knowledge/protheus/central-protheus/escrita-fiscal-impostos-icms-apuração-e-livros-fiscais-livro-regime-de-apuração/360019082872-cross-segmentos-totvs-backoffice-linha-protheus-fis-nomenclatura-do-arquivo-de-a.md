---
article_id: 360019082872
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: c4c26ecf4c7607a65872793dd1d4551bd30d656959ca9112cf2a2867c8c45ab7
fetched_at: '2026-06-28T22:39:22.172385+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Nomenclatura do Arquivo
  de Apuração de Impostos
type: support-article
updated_at: '2024-01-11T18:01:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019082872-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Nomenclatura-do-Arquivo-de-Apura%C3%A7%C3%A3o-de-Impostos
---

**Dúvida**

Como é composto a a nomenclatura do arquivo de apuração de impostos  
  
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
   
**Solução**  
Ao realizar a apuração de ICMS ou IPI o sistema, por padrão, salva um arquivo na pasta SYSTEM do sistema, este arquivo obedece a configuração abaixo:  
  
A – Número do Livro Selecionado, se for \* o Sistema fixa a letra A, se no cadastro do TES for informado o número do livro e nos parâmetros da Apuração for informado o número do livro de 1 à 9 ele preenche com o próprio número do livro 1F010101.IC0.  
  
AA010101.IC0  
  
A – Mês de apuração de ICMS/IPI, conforme tabela abaixo:  
  
A Janeiro;   
B Fevereiro;   
C Março;   
D Abril;   
E Maio;   
F Junho;   
G Julho;   
H Agosto;   
I Setembro;   
J Outubro;   
K Novembro;   
L Dezembro;   
S Semestral;   
X Anual.  
01 – Ano de apuração, últimos 2 dígitos.  
01 – Código da Empresa.  
  
IC\* - Extensão do Arquivo, IC – ICMS, IP – IPI, CP - PIS e COFINS, IS - ISS:  
\* 1 – Primeiro Decêndio  
\* 2 – Segundo Decêndio  
\* 3 – Terceiro Decêndio  
\* 0 – Mensal  
\* 1 – Primeira Quinzena  
\* 2 – Segunda Quinzena  
  
Observando as informações Exemplo: AA010101.IC0;  
  
Entende-se:  
  
A - LIVRO  
l - MÊS  
12 - ANO  
02 - COD. DA EMPRESA  
03 - COD. DA FILIAL  
.ic0, .ip0, cp0 ou is0
