---
article_id: 31766720629527
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 5e242a1d8008a6b5a95cc32e170f267083de003e224988bdf8f7cd9964bfd693
fetched_at: '2026-06-28T22:38:28.775683+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Alterar o tamanho de um campo
  no faturamento (FAT)
type: support-article
updated_at: '2025-04-30T17:39:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31766720629527-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Alterar-o-tamanho-de-um-campo-no-faturamento-FAT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31766680850071) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como alterar o tamanho de um campo no faturamento (FAT)?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

**OBSERVAÇÃO 1:** Dúvidas nesse processo, contate a Equipe Framework

**OBSERVAÇÃO 2:** O tamanho de um campo pode ser sempre aumentado (respeitando o limite) mas, nunca deve se tornar menor do que era para não ser perdido informações no banco de dados

**OBSERVAÇÃO 3:** Caso o campo tenha grupo de campos (numérico ou não), o grupo todo pela integridade deve ser alterado ([Grupo de Campos Numéricos](https://tdn.totvs.com/x/JVo9L))

**OBSERVAÇÃO 1:** Campos são chamados em colunas no banco de dados

1) Para alterar o tamanho de algum campo da rotina, identifique primeiramente o nome do campo. Para isso, clique sobre o campo e pressione F1

![](https://tdn.totvs.com/download/attachments/271400228/TC_01.png?version=1&modificationDate=1486045551000&api=v2)

2) Após verificar o nome do campo, siga o procedimento abaixo:  
- Acesse Configurador > Base de Dados > Dicionário > Bases de Dados  
- Clique em Dicionário de Dados, selecione a tabela do campo, e clique em Editar

![TC_02.png](https://tdn.totvs.com/download/attachments/271400228/TC_02.png?version=1&modificationDate=1486045551000&api=v2)

3) Expanda a tabela, clique em Campos e localize o campo que vai alterar  
- Clique sobre o campo e clique em Editar

![TC_03.png](https://tdn.totvs.com/download/attachments/271400228/TC_03.png?version=1&modificationDate=1486045551000&api=v2)

4) Em Tamanho, digite o novo tamanho do campo e clique em Salvar

![TC_04.png](https://tdn.totvs.com/download/attachments/271400228/TC_04.png?version=1&modificationDate=1486045551000&api=v2)

5) Na tela da listagem de campos, clique em Confirmar (seleção)

- Na tela da listagem de tabelas, clique em Atualizar base de dados

![TC_05.png](https://tdn.totvs.com/download/attachments/271400228/TC_05.png?version=1&modificationDate=1486045551000&api=v2)

**Aviso:**

Este procedimento de "Atualizar base de dados" tem por finalidade confirmar a inclusão do campo na tabela no banco de dados. Este procedimento deve ser feito em modo exclusivo, ou seja, não pode haver nenhum usuário com alguma rotina aberta que utilize a tabela envolvida.

6) Na tela Atualização do Dicionário de Dados, clique em Avançar

![TC_06.png](https://tdn.totvs.com/download/attachments/271400228/TC_06.png?version=1&modificationDate=1486045551000&api=v2)

7) Na próxima tela, clique em Avançar novamente  
- Aguarde o processamento. Ao final, será exibida uma tela como essa, indicando Atualização finalizada com sucesso. Clique em Finalizar.

![TC_07.png](https://tdn.totvs.com/download/attachments/271400228/TC_07.png?version=1&modificationDate=1486045551000&api=v2)

**Saiba mais:**

[Campos - Como alterar o tamanho](https://tdn.totvs.com/x/JD0tE)
