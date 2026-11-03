---
article_id: 360026219912
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 0a91ce1a6a2a30fefc76e72dfaf8d3082035beb8d13b91d883d8bfe4639a0cd6
fetched_at: '2026-06-28T22:42:10.368728+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Configuração
  GI ICMS - Rotina  MATA965
type: support-article
updated_at: '2023-07-11T13:24:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026219912-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Configura%C3%A7%C3%A3o-GI-ICMS-Rotina-MATA965
---

**Dúvida**Configuração GI ICMS - Rotina MATA965  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Esta rotina permite configurar a impressão do mapa auxiliar no preenchimento da GI-ICMS (Guia de Informação das Operações e Prestações Interestaduais) e do antigo DMEF (Demonstrativo do Movimento Econômico e Fiscal).

Essa configuração define, a cada operação, a indicação dos CFOs (Códigos Fiscais de Operação) correspondentes utilizados nas notas fiscais, além dos critérios de seleção de itens que pertençam a determinadas classes fiscais.

O critério de seleção pode ser preenchido em linguagem AdvPl, criando assim uma espécie de filtro que, conforme indicado na sintaxe, “varre” o sistema em busca das informações.

Após esta configuração, os dados atribuídos aos campos são gravados no arquivo “SIGADMEF.CPF”, que será utilizado pelos programas de relatórios, os quais necessitam de sintaxe AdvPl para que o sistema selecione os registros específicos.

A impressão da GI-ICMS considera este mesmo arquivo, verificando o campo “998”, referente a “Petróleo” e “Combustível”, não utilizado pela DMEF.

**Procedimentos de Configuração**

**Para efetuar a configuração da GI-ICMS:**

1. No módulo **Livros Fiscais (SIGAFIS)** acesse **Miscelanea/Arq. Magneticos/Config GI - ICMS (MATA965)**, o sistema apresentará a tela de parâmetros da rotina, que permite selecionar para configuração:  
     GI-ICMS/DMEF  
     DCP - Instrução Normativa 69  
     DMA  
     CADPRO
2. Selecione e confirme.  
     O sistema abre uma tela relacionando os campos e critérios de seleção de dados para a configuração.  
     De acordo com a seleção, o sistema apresenta uma tela diferente para configuração da impressão do mapa. Tomaremos como exemplo os itens de configuração da GI-ICMS/DMEF.
3. Posicione o cursor sobre o sub-item do grupo dos campos apresentados e tecle [Enter], ou dê um clique duplo sobre o item selecionado.  
     Será apresentada uma tela solicitando os CFOs correspondentes.
4. Observe os itens descritos nos grupos de campos organizados, para informar o CFO (Código Fiscal da Operação) respectivo.  
     Os grupos a serem informados os CFOs são os seguintes:  
     ***Campos Referentes a Entradas e Aquisições***  
     Neste campos apresentam-se as possíveis transações com entradas e aquisições de:  
        • Matéria-prima/Material Secundário/Embalagens/Serviços  
        • Produtos referentes a produção própria  
        • Mercadoria para Revenda  
        • Energia Elétrica  
        • Serviços de Comunicação  
        • Serviços de Transporte  
     
     ***Campos Referentes a Saídas e Prestações***  
     Nestes campos apresentam-se as possíveis transações com saída e prestações de:  
        • Matéria-prima/Material Secundário/Embalagens/Serviços  
        • Produtos referentes a produção própria  
        • Mercadoria para Revenda  
        • Energia Elétrica  
        • Serviços de Comunicação  
        • Serviços de Transporte  
      
    ***Campos Referentes a Industrialização***  
     
     Nestes campos apresentam-se as possíveis transações com industrialização de materiais:  
        • Por Terceiros deste Estado  
        • Por Terceiros de outros Estados
5. Observe os itens descritos nos grupos de campos organizados, para informar o Critério de Seleção de Dados, através de sintaxe AdvPl, conforme indicado no início deste capítulo:  
   ***Campos Referentes a Estoques Próprios***  
     Neste campos apresentam-se as possíveis movimentações do estoque, sendo:  
        • Matéria-prima/Material Secundário/Embalagens/Serviços  
        • Produtos referentes a produção própria  
        • Mercadoria para Revenda  
        • Produtos em Elaboração  
     
     ***Campos Referentes a Petróleo***  
       
   Nestes campos apresentam-se as possíveis transações com petróleo realizados por sua empresa, sendo:  
        • Petróleo  
     
     ***Campos Referentes a Não Contribuintes***  
     Nestes campos apresentam-se as possíveis transações com os considerados não contribuintes, sendo:  
        • Não Contribuintes
6. Observe o seguinte item descrito nos grupos de campos organizados, para informar o Critério de Seleção das contas contábeis:  
     
     ***Campos Referentes a Informações Contábeis***  
     Nestes campos apresentam-se as possíveis informações contábeis referentes às movimentações dos módulos, sendo:  
        • Saldo no Início do Período  
        • Movimento no Período
7. Após as configurações, confirme a rotina.
