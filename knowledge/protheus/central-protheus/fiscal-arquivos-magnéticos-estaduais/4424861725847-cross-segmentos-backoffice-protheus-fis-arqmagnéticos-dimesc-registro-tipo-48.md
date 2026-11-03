---
article_id: 4424861725847
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 67e9e71c29c7c6cfa12797426c7e9f66ce876b2670a499a1b32c0ae94afe4b15
fetched_at: '2026-06-28T22:42:10.807439+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DIMESC - Registro
  tipo 48
type: support-article
updated_at: '2022-08-17T19:39:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4424861725847-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DIMESC-Registro-tipo-48
---

**Dúvida**

DIMESC - Registro tipo 48  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - Todas as versões  
  
**Solução**

**Registro tipo 48 – Receita de prestação de serviço e fornecimento de energia elétrica**  
Tem como base as informações do Livro Fiscal relacionado com os parâmetros MV\_RG48001, MV\_RG48002, MV\_RG48003, MV\_RG48004, MV\_RG48005, MV\_RG48006, MV\_RG48007, MV\_RG48008, MV\_RG48501 e MV\_RG4850.

**Importante:**

Para o campo **Código de Atividade** atualmente há tratativa apenas para os códigos 001/002/003/004/005/006/007/008/501/502/503/504/505/506 através dos parâmetros MV\_RG48003, MV\_RG48004, MV\_RG48005, MV\_RG48006, MV\_RG48007, MV\_RG48008, MV\_RG48501, MV\_RG48502, MV\_RG48503, MV\_RG40504, MV\_RG48505, MV\_RG48506, onde é apontado os códigos do Tipos de Atividades e também o conteúdo do campo indicado no parâmetro **MV\_CMUNSCC**  que indica o município da prestação do serviço em SC .

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4424855391127/mceclip1.png)

Para o Registro tipo 48 da DIME o código do **Tipo de Atividade 011 (para quantidade de energia elétrica de fonte hidráulica produzida no mês)** existe no leiaute como opção, porém não tem tratativa e nenhum parâmetro para o código do Tipo de Atividade 011.  
  
Nos casos de Norma de Segmento Especifico a TOTVS, não possui obrigatoriedade de implementar no padrão do sistema, visto que o mesmo é específico e direcionado exclusivamente ao segmento de negocio do cliente.  
  
Porém temos o ponto de entrada **DMSC48TP** para que possa realizar a alteração no registro 48 e gerar o código Tipo de Atividade 011.

Documentação do Ponto de entrada  
<https://tdn.totvs.com/x/6CCcJQ>

**Assuntos relacionados:**

DT PE DIMESC Criação de Ponto de Entrada para registro Tipo 48 gerar código do Tipo de Atividade 011  
<https://tdn.totvs.com/pages/viewpage.action?pageId=630991584>  
  
Procedimento para Configuração da DIMESC- Declaração de ICMS e do Movimento Econômico do Estado de Santa Catarina  
<https://tdn.totvs.com/pages/viewpage.action?pageId=655881026>

FAQ Consultoria de Segmentos TOTVS - Dime SC - Quadro 48 - Quando Gerar

<https://tdn.totvs.com/display/public/ConSeg/Dime+SC+-+Quadro+48++-+Quando+Gerar>
