---
content_hash: 60c24e5189801358bae6c3589223f91048adf599a6f42e44e12168e3d6afbaa6
fetched_at: '2026-06-29T00:09:08.524008+00:00'
page_id: '389552455'
product: rm
source: tdn-rm
title: 3282491 FISCAL01-5893 DT NF-e - Geração do Grupo impostoDevol
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=389552455
version: 9
---

# NF-e - Geração do Grupo impostoDevol

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Emissão de NF-e |
| **Situação/Requisito:** | Ao gerar uma NF-e de Devolução é necessário gerar o grupo de impostos devolvidos |
| **Solução/Implementação:** | O processo de emissão da NF-e foi alterado para gerar o grupo UA. Tributos Devolvidos (para o item da NF-e) conforme as regras do manual de integração do contribuinte v 6.00 e NT 20016.002 v 1.60  Manual de Orientação do contribuinte V 6.00  NT 2016.002 v 1.60  **Cadastro da Natureza de Operação**  Para gerar o grupo de devolução de imposto (impostoDevol) a natureza deverá ser cadastrada conforme abaixo   1. Tipo de Devolução deverá ser configurado como devolução (Figura 1) 2. A Regra de IPI estiver definida como outros (Figura 2) 3. CST do IPI deverá ser 99 - Outras Saídas (Figura 3)   Figura 1  Figura 2  Figura 3  **Criação do movimento**   1. O movimento deverá ser criado utilizando o motivo de referência 4 - Devolução de Compra de Mercadorias (Figura 4) 2. Ao salvar o movimento deverá ser ajustado os itens e as quantidades que estão sendo devolvidas 3. Em cada item devolvido deverá ser destacado o IPI Devolvido (Figura 5)     Figura 4  Figura 5  **Envio da NF-e**  Para cada item na nota de devolução serão geradas as TAGs abaixo.   1. pDevol (Percentual da mercadoria devolvida): Será gerado com o resultado da quantidade do item da nota de devolução dividido pela quantidade do item da nota de compra. **Exemplo**: 2. vIPIDevol( Valor do IPI devolvido): Será gerado com o valor do IPI destacado no item da nota de devolução.   Exemplo do XML: xmlUA. Tributos Devolvidos (por item) 71,43  25.00 ]]> |
