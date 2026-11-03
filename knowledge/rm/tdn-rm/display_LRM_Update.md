---
content_hash: 8b4ee8fe967ebf7e7f5d2e0f63f4350ec955d75918342b936309717af50822a9
fetched_at: '2026-06-29T00:05:59.761456+00:00'
page_id: '192090482'
product: rm
source: tdn-rm
title: Update
type: documentation
url: https://tdn.totvs.com/display/LRM/Update
version: 12
---

Os serviços do Corpore RM com as funcionalidades para utilização do TOTVS | HTML Framework estarão disponíveis em 2016. No momento versões controladas serão disponibilizadas para as equipes de Segmentos envolvidas no projeto de Experiências de Uso

Versão

 Disponível à partir da versão 12.1.6 da linha RM.

# Update

Atualiza um registro no dataserver. Esse método pode ser acionado através de uma requisição do tipo PUT e no corpo dessa requisição deve constar o json com os dados a serem alterados. Após a alteração o método retornará uma mensagem confirmando a operação ou mostrando os erros ocorridos.

## Exemplo de utilização

Método: PUT

URL: <http://localhost:8051/rmsrestdataserver/rest/GlbDeptoData/1$_$1$_$99>

### Corpo da requisição

### Resposta da requisição

Atenção

Para **deletar** itens que não são da tabela **master** do registro é necessário adicionar ao JSON da requisição a "coluna" "$state"  com valor 3, **para cada linha do registro "filho" ou "master" que deseja alterar.**

Ao inserir a coluna $state o sistema irá entender para cada linha que o estado da Linha(**Row**) será representada pela ação conforme tabela abaixo.

| Coluna | Valor | Ação |
| --- | --- | --- |
| $state | 0 | Inalterada |
| $state | 1 | Inserida |
| $state | 2 | Modificada |
| $state | 3 | Deletada |

Exemplo:

        {  
          "id": "A$\_$\_me\_1FeriasNet",  
        "CODSISTEMA": "A",  
        "CODPERFIL": "\_me\_1FeriasNet",  
        "NOME": "Menu de permissao .Net (Chronus)",  
        "STATUS": 1,  
        "CONTROLE": -29491,  
        "INTEGRADOFLUIG": null,  
        "IDPERFIL": "\_me\_1FeriasNet\_A",  
        "PROTECTEDDATAACCESS": 1,  
        "APLICACOES": null,  
        "GAUTZMENU": [  
            {  
                "id": "A$\_$\_me\_1FeriasNet$\_$9",  
                "parent\_id": "A$\_$\_me\_1FeriasNet",  
                "CODSISTEMA": "A",  
                "CODPERFIL": "\_me\_1FeriasNet",  
                "TAGMENU": 9,  
                "PERMISSOES": "\*\*\*\*",                
                "CONTROLE": -16776,

**"$state" : 3**  
            }]

      }
