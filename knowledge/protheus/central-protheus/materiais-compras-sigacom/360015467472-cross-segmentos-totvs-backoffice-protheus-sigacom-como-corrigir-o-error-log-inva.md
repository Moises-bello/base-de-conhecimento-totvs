---
article_id: 360015467472
category: Materiais - Compras (SIGACOM)
content_hash: d357a89837b57b005f9709ebe43158470468d1e32e5261874e2603c645faf1fa
fetched_at: '2026-06-28T22:41:07.587566+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como corrigir o error
  log Invalid field name in Alias
type: support-article
updated_at: '2023-05-18T17:14:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015467472-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-corrigir-o-error-log-Invalid-field-name-in-Alias
---

**Dúvida**Como corrigir o error log Invalid field name in Alias

Exemplos de ocorrências:

Invalid field name in Alias SA2->A2\_DEDBSPC on FWMBROWSE:GETCBOX(FWMBROWSE.PRW)

Invalid field name in Alias SF1->F1\_CLIPROP on MAATUSB6(COMXFUN.PRX)

Etc.

**Ambiente**Protheus – Compras – A partir da versão 12.17  
  
**Solução**O erro Invalid field name in Alias indica que determinado campo está inválido, ou seja, por alguma razão, não foi encontrado para ser consultado/manipulado.

Possíveis causas:  
  
1 - O campo não está marcado como Usado no dicionário (configurador), ou, não está flegado como disponível para o Módulo em questão. Necessário validar a configuração do campo, de acordo com o dicionário padrão, e confirmar o ajuste do campo no Configurador;

2 - O nível de campo está superior à configuração do usuário em questão que está realizando o procedimento, ou seja, o usuário não possui "acesso" ao campo devido configuração de nível. Ajustar a configuração do nível do campo conforme dicionário padrão, e confirmar o ajuste do campo no Configurador;

3 - O campo está criado, e devidamente configurado no dicionário de dados (SX3), porém, não está criado no banco de dados. Ou seja, na visualização do banco, não localiza a coluna destinada a este campo (inclusive com a correta configuração de Filiais, se for o caso). Campo está criado somente no dicionário, mas não no banco de dados;

Neste caso, é necessário recriar a tabela no banco de dados, de acordo com o dicionário (SX3) padrão. Este procedimento não é suportado pelo Suporte Protheus, visto se tratar de uma inconsistência no banco de dados, e não sistêmica, porém, segue abaixo uma alternativa para o procedimento, o qual deve ser realizado em ambiente/base de teste, exclusivamente por consultor habilitado para procedimentos de manutenção de banco de dados, após backups do ambiente e banco.

- Backup do ambiente e do banco de dados, principalmente da tabela em questão;

- Conferir que o arquivo de backup está adequado e não foi corrompido;

- Dropar a tabela em questão;

- Abrir novamente o Protheus e a rotina que manipula a tabela. Neste momento, o sistema automaticamente irá recriar a Tabela no banco de dados com base no dicionário de dados;

- Appendar os dados do backup na Tabela;

Obs: Registros já gravados sem conteúdo no campo não são afetados / preenchidos automaticamente por este procedimento, sanado assim o problema apenas para novos registros que o sistema irá gravar.
