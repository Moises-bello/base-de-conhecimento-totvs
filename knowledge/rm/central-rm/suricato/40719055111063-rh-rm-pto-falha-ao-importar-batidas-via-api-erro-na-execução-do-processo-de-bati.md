---
article_id: 40719055111063
category: Suricato
content_hash: 1bb479ac065a4d6ad4433a121b35122a7699d2fcc91d6d66b1b0765776299b63
fetched_at: '2026-06-28T22:46:26.315416+00:00'
product: rm
section_id: 28312167464215
source: central-rm
title: 'RH - RM - PTO - Falha ao importar batidas via API: "Erro na execução do processo
  de batida"'
type: support-article
updated_at: '2026-05-25T17:50:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40719055111063-RH-RM-PTO-Falha-ao-importar-batidas-via-API-Erro-na-execu%C3%A7%C3%A3o-do-processo-de-batida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40719055101079) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao executar o processo de importação de batidas, selecionando o parâmetro "Utilizar integração com o TSA" é retornado a mensagem de erro: "**Erro na execução do processo de batida**"  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/40719055102743)**  
  
**Ambiente**  
TOTVS RH - TOTVS RH(Linha RM) - Automação de Ponto - Todas Versões  
  
**Solução**  
Esse erro ocorre, quando algum campo obrigatório das tabelas responsáveis pelo armazenamento das batidas (**AINTEGRACAOBATIDAS** ou **MSA\_CONTROL\_MARCAC**) não foi preenchido ou está com formato inválido.

Para validar as informações gravadas, execute as consultas abaixo:

```
select * from AINTEGRACAOBATIDAS
select * from MSA_CONTROL_MARCAC
```

Após carregar os registros via banco de dados, verifique se todos os campos obrigatórios foram preenchidos corretamente e se os dados seguem o formato esperado pela API.

Para consultar o mapeamento dos campos, obrigatoriedades e formatos aceitos, acesse a documentação oficial:

<https://tdn.totvs.com/display/public/LRM/Campos+da+API>

Seguindo o padrão informado na documentação, a importação das batidas será processada corretamente.

**Saiba Mais**  
[RH - RM - PTO - Importação de batidas via API de integração com Suricato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13618422681367-RH-RM-PTO-Importa%C3%A7%C3%A3o-de-batidas-via-API-de-integra%C3%A7%C3%A3o-com-Suricato)
