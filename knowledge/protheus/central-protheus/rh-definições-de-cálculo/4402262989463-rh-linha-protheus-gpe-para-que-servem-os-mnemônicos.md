---
article_id: 4402262989463
category: RH - Definições de Cálculo
content_hash: 9240d0b7415640e1029ad6fd0abe7850ed7d2841d3ce84d53323bc145abd4116
fetched_at: '2026-06-28T22:43:22.490754+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Para que servem os mnemônicos
type: support-article
updated_at: '2025-08-20T18:56:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402262989463-RH-Linha-Protheus-GPE-Para-que-servem-os-mnem%C3%B4nicos
---

**Dúvida**Para que servem os **mnemônicos**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Os **Mnemônicos** são variáveis utilizadas na escrita de um programa. Neste cadastro são armazenadas todas as variáveis que estão disponíveis para serem utilizadas na elaboração de **Fórmulas, Roteiros de Cálculo e Biblioteca de Funções**.  
  
Os mnemônicos relacionados neste cadastro são classificados conforme legenda:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11253491122711)

Os mnemônicos de Sistema ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11253530093207) não podem ser alterados, nem excluídos, somente podem ser visualizados.

**Principais Campos e Controles**• **Código**: Nome do Mnemônico ou variável que será utilizado no Roteiro de Cálculo, Cadastro de Fórmulas e Biblioteca de Funções.  
Os Mnemônicos cadastrados pelo usuário devem ser da forma: M\_<NomeMnemonico>.  
Exemplo: M\_VALORSAL, M\_HEXTRA.  
  
• **Descrição**: Informe a descrição do mnemônico.  
  
• **Tipo de Mnemônico**: Neste campo deve ser informado o Tipo do Mnemônico, entre as opções: "A - *Array*", "B - Bloco", "C - Caractere", "D - Data", "L - Logico", "N - Numérico", "O - Objeto" ou "U - Indefinido".  
  
• **Conteúdo**: Informe dado/valor/data, etc. com que o mnemônico deve ser inicializado para a utilização no Roteiro de Cálculo ou Formulas.  
Exemplo:  
Tipo Lógico -> .T.  
Tipo Caractere -> AB  
Tipo Numérico -> 0  
  
• **Tipo de Variável**: Determina qual o tipo de variável que o mnemônico será definido: "1 - Pública", "2 - Privada" ou "3 - Local"
