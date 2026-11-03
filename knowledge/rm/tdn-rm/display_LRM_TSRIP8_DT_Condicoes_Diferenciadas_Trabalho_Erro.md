---
content_hash: f60c3035bad9173ac9bd0b070a840ad9a488d0466043106ae724bb3f0da030df
fetched_at: '2026-06-29T00:06:04.747883+00:00'
page_id: '200911008'
product: rm
source: tdn-rm
title: TSRIP8_DT_Condicoes_Diferenciadas_Trabalho_Erro
type: documentation
url: https://tdn.totvs.com/display/LRM/TSRIP8_DT_Condicoes_Diferenciadas_Trabalho_Erro
version: 4
---

# CONDIÇÕES DIFERENCIADAS DE TRABALHO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Função:** | *Condições Diferenciadas de Trabalho* |
| **Situação/Requisito:** | *Ao editar o cadastro do funcionário e ir em Anexos / Segurança e Medicina / Condições Diferenciada de Trabalho, é retornado o erro: Ocorreu um erro ao efetuar a leitura da visão:*  *A coluna 'CODCOLIGADA, CHAPA, CODTPCONDDIFTRAB, DATAINICIO' está restrita a conter valores exclusivos. O valor 'X, YYY, ZZ, DD/MM/YYYY' já existe* |
| **Solução/Implementação:** | *Foi ajustado o serviço que valida se já existe alguma condição diferenciada de trabalho com a mesma data.* |
| **Chamados relacionados:** | *TSRIP8* |
| **Versões/Release:** | *12.1.7* |
