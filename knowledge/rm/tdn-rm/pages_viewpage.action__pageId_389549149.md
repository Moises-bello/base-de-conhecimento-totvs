---
content_hash: 5e5e4da5ab3c2ac79e003cb8c7398bdcfdc3ed65ce89e5975e0e38462bacfa7b
fetched_at: '2026-06-29T00:09:08.475909+00:00'
page_id: '389549149'
product: rm
source: tdn-rm
title: 3334602 FOPCALCULO01-4289 Afastamento por Licença Maternidade Complementar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=389549149
version: 1
---

# Afastamento Licença Maternidade Complementar

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Cadastro de Funcionários | Afastamento |
| **Situação/Requisito:** | Quando o funcionário está com afastamento por Licença Maternidade (Tipo E) e é feito a inclusão do afastamento tipo W (Licença Maternidade Complementar) após o termino do período de afastamento pelo tipo E, o sistema não está permitindo, retornando a mensagem: "Erros ao gravar dados: Não foi possível criar um novo registro no Histórico de Afastamento. Já existe um afastamento que a data coincide com a data de mudança da nova situação do funcionário. Verifique a data da mudança da situação e o histórico de afastamento". |
| **Solução/Implementação:** | Ajustado a validação de duplicidade de registro no Histórico de Afastamento por Licença Maternidade, que não estava permitindo inserir um novo, mesmo que as datas não tivessem intercessão. |
| **Tickets relacionados:** | 3334602 |
