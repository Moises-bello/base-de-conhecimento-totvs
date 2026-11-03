---
article_id: 360041296033
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: b5a356dd282ec3c61adf5e54bc9b9450181067fb8dfa602eaee7c0a3c6d1e8e8
fetched_at: '2026-06-28T22:42:03.853502+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: MP - FIS - Validação e Tratamento das Espécies Conforme Tabela 4.1. SPEDFISCAL
type: support-article
updated_at: '2021-04-28T14:25:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041296033-MP-FIS-Valida%C3%A7%C3%A3o-e-Tratamento-das-Esp%C3%A9cies-Conforme-Tabela-4-1-SPEDFISCAL
---

**Dúvida**  
Parametrização, validação e tratamento das Espécies realizada pelo Microsiga Protheus conforme tabela 4.1.1 do Ato Cotepe nº 9, de 18 de Abril 2008 para arquivo magnético SPEDFISCAL.  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

M. Protheus trata da seguinte forma as especies e os modelos de cada nota, para ser apresentada no arquivo magnético SPEDFISCAL.

MODELOS DE DOCUMENTOS, Abaixo a relação das notas que são tratadas pelo sistema:

Espécie = "CA" modelo "10" // Conh.Aereo  
Especie = "CTA" modelo "09" // Conh.Transp.Aquaviario  
Especie = "CTF" modelo "11" // Conh.Transp.Ferroviario  
Especie ="CTR" modelo "08" // Conh.Transp.Rodoviario  
Especie="NFST" modelo "07" // NF Servico de Transporte  
Especie="CTM" modelo "26" // Conh.Transp.Multimodal  
Especie = "CTE" modelo ="57" // Conhecimento de Transporte Eletronico  
Espécie="CTEOS" modelo "67" //Conhecimento de Transporte Eletrônico para Outros Serviços - CT-e OS  
Especie = "NFPS" modelo " " // NF Prestacao de Servico  
Especie="NFS" modelo " " // NF Servico  
Especie="RPS" modelo " " // Recibo Provisorio de Servicos - Nota Fiscal Eletronica de Sao Paulo  
Especie="NFSC" modelo "21" // NF Servico de Comunicacao  
Especie="NTST" modelo"22" // NF Servico de Telecomunicacoes  
Especie="NFCF" modelo "02" // NF de venda a Consumidor Final  
Especie="CF" .ou "ECF" modelo "02" // Cupom Fiscal gerado pelo SIGALOJA  
Especie="RMD" modelo "18" // Resumo Movimento Diario  
Especie = "NFCEE" modelo "06" // Conta de Energia Eletrica  
Especie ="NFFA" modelo "29" // Nota fiscal de fornecimento de agua  
Especie="NFCFG" modelo "28" // Nota fiscal/conta de fornecimento de gas  
Especie = "NFE" modelo "01" // NF Entrada  
Especie ="NFA" modelo ="1B" // Nota Fiscal Avulsa  
Especie="NFP" modelo "04" // NF de Produtor  
Especie="SPED" modelo "55" // Nota fiscal eletronica do SEFAZ.  
Especie="NFCE" modelo "65" // Nota fiscal Eletronica ao Consumidor Final  
Especie="SATCE" modelo "59" //CUPOM FISCAL ELETRÔNICO – SAT

Qualquer espécie informada na nota que não esteja na relação acima será considerada como modelo 01 (NFE), ou seja, se criar uma espécie de nome "NOTA" e vincular a alguma nota de entrada ou saída, esta espécie será interpretada como modelo 01 no Sped Fiscal.

Caso queira criar uma nova espécie e vincular a um código é necessário utilizar ponto de entrada, MTMODNOT - Retorna código do modelo de doc. fiscal :  
Para maiores informações sobre ponto de entrada acesse: http://tdn.totvs.com/pages/releaseview.action?pageId=6077102

No SPED FISCAL, o campo F3\_ESPECIE e FT\_ESPECIE é quem irá determinar o código que será gerado no Sped fiscal. Caso esteja preenchido como 'SPED' será gerado no Sped Fiscal como modelo 55.

Lembrando que para vincular uma espécie a uma serie é necessário utilizar o parâmetro MV\_ESPECIE.  
Exemplo de preenchimento para serie 001, cadastrada na tabela 00 chave 01 no configurador em cadastro, tabelas: 001= SPED;

Para cadastrar uma nova espécie é necessário utilizar a tabela 42 chave 1 da SX5 no configurador, cadastro, tabelas.

Desta forma, todas as notas de serie 001 serão geradas na SFT e SF3 como espécie SPED e modelo 55 no Sped Fiscal.

Para dúvidas de como customizar utilizando ponto de entrada MTMODNOT entre em contato com N1\_ADVPL.

Link contendo fonte das informações acima:

<https://tdn.totvs.com/pages/releaseview.action?pageId=374315189>
