---
article_id: 360050767514
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 2fd655854db33a50d00572276d812aeaf5f31bb61e5998f198eec489ceccd2ed
fetched_at: '2026-06-28T22:42:03.783240+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: MP - FIS - Espaçamento Indevido no Campo Produto - SPED FISCAL e EFD Contribuições
type: support-article
updated_at: '2021-04-28T14:25:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050767514-MP-FIS-Espa%C3%A7amento-Indevido-no-Campo-Produto-SPED-FISCAL-e-EFD-Contribui%C3%A7%C3%B5es
---

**Dúvida**  
Ao gerar o arquivo magnético de ambas as obrigações fiscais (SPED FISCAL/ EFD Contribuições) é apresentado um espaçamento indevido no campo produto referente o bloco 0.    
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
Referente o problema mencionado, será necessário verificar o conteúdo do parâmetro MV\_COFLSPD:

**MV\_COFLSPD**  
  
Informe .F. para não concatenar o código da filial nos códigos dos registros do SPED Fiscal e SPED Contribuições.  
  
Por padrão a filial é sempre concatenada nos registros de códigos do bloco zero, porém se houver a necessidade de que estes códigos não mais serem gerados concatenados com código da filial, então este parâmetro MV\_COFLSPD deverá ser criado manualmente e informar conteúdo .F.

Procedimentos para criar o parâmetro:

**Nome da Variável:** MV\_COFLSPD

**Tipo:** Logico

**Conteúdo:** .F.

**Descrição:** Informe .F. para não concatenar o código da filial nos códigos dos registros do SPED Fiscal e SPED Contribuições  
  
Se este parâmetro não existir na dicionário de dados, por padrão o código da filial será concatenado nos códigos dos registros do bloco zero.

**Nota:**  
Além da configuração do parâmetro acima, temos histórico de atendimento referente o problema de espaçamento por motivo do produto ser cadastrado com espaço a mais ou na utilização da função copia e cola (CTRL+C e CTRL+V) no momento do cadastro, por conta disso, ao gravar o produto o mesmo é gravado com espaços.
