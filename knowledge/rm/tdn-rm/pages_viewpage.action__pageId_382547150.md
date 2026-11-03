---
content_hash: ba7a99a06de21d3592438d9c0443905cae7ef87ea48640841cf0d73ee54250ba
fetched_at: '2026-06-29T00:09:04.058785+00:00'
page_id: '382547150'
product: rm
source: tdn-rm
title: Como cadastrar as informações que compõem o evento S-2250 - Aviso Prévio?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=382547150
version: 1
---

Para cadastrar as informações que compõem o evento S-250, o usuário deve acessar o cadastro de funcionário e selecionar a opção "Aviso Prévio Trabalhado":

Os campos do cadastro devem ser preenchidos conforme as orientações abaixo:

**Tipo de Demissão**

Serão apresentados os tipos que correspondem as demissões por iniciativa do empregador ou do empregado, ambas sem justa causa, e comum acordo.

> Serão listados os seguintes tipos:
>
> 2 - Inic. Empregador sem justa causa"  
> 4 - Inic. Empregado sem justa causa
>
> V - Comum acordo

**Data de Início do Aviso**  
Preencher com a data de início do aviso prévio.

**Data de Demissão Prevista**Preencher com a data prevista de desligamento.

> Observação: A data informada deve ser igual ou superior ao inicio do aviso prévio.

**Tipo de Redução Aviso**  
Caso o tipo de demissão seja "2 - Inic. Empregador sem justa causa" ou "V - Comum Acordo", será habilitado a opção "Dias" e "Jornadas", permitindo a redução do aviso conforme previsto em lei.

**Forma Redução Aviso**Disponível para os tipos de demissão "2 - Inic. Empregador sem justa causa" e "V - Comum Acordo", deverá informar se a forma de redução do aviso será pelo Início ou pelo Fim. Caso não marque nenhuma, será considerado pelo Início.

**Tipo de Aviso Prévio**

Indica quem avisou o desligamento.

**Motivo da Mudança**

Informar o motivo da mudança que será gravado no histórico de situação do funcionário.

Observação: Após o cadastramento do aviso prévio individual ou coletivo, a situação do funcionário será alterada para "V - Aviso Prévio".

**Gerar Log Consolidado**

Marcando este parâmetro, será gerado um log mais detalhado no processo de Aviso Prévio Coletivo em um arquivo txt onde constará:

1. Motivo pelo qual não foi possível cadastrar aviso prévio a um funcionário.
2. Totalizadores por seção e de todo o processo.

Caso não seja definido um caminho para salvar o arquivo, será salvo no caminho parametrizado no Parametrizador/Folha Normal/Geral/Diretório Utilizado para Processos que geram arquivos em .net (Jobserver).

Se não for definido caminho em nenhum dos campos citados acima, será gerado na pasta RM.Net.

Ao marcar a flag **Incluir Avisos Cadastrados no Log**, será imprimido no log, também os avisos que foram cadastrados com sucesso.

**OBS:** Processo disponível apenas no cadastro de aviso prévio **coletivo**.
