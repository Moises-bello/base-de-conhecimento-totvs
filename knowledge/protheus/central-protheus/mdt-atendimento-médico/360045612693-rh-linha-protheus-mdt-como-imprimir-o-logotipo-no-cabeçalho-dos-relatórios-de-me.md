---
article_id: 360045612693
category: MDT - Atendimento Médico
content_hash: 34d75834f79135eda15b7c761151162024e644232e824b64442afa3d977aaa34
fetched_at: '2026-06-28T22:44:20.652868+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Como imprimir o logotipo no cabeçalho dos relatórios
  de Medicina e Segurança do Trabalho
type: support-article
updated_at: '2025-08-14T19:03:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045612693-RH-Linha-Protheus-MDT-Como-imprimir-o-logotipo-no-cabe%C3%A7alho-dos-relat%C3%B3rios-de-Medicina-e-Seguran%C3%A7a-do-Trabalho
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27597590619415)**Tempo aproximado para leitura: 00:01:00 min  
 **Dúvida**Como imprimir o logotipo no cabeçalho dos relatórios de Medicina e Segurança do Trabalho?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**1. Faça a criação de um arquivo com o logotipo seguindo a seguinte nomenclatura e extensão:  
LGRL + Codigo da Empresa + Filial + .BMP  
  
2. O arquivo deve ser salvo no diretório system. Caso a filial não seja indicada na nomenclatura do arquivo o logotipo será considerado para TODAS as filiais.  
  
**Exemplo:**   
LGRL0101.BMP  (Logotipo da Empresa 01, Filial 01)  
LGRL03.BMP    (Logotipo da Empresa 03 para todas as filiais)  
  
As configurações abaixo são obrigatórias:

* Logotipo deve obedecer o tamanho de 100 pixels de largura por 20 de altura;
* O arquivo deve ser salvo como BITMAP DE 256 CORES.

No diretório system existe o arquivo LGRL99.BMP que pode ser utilizado como exemplo para dimensionamento do arquivo.  
  
**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
