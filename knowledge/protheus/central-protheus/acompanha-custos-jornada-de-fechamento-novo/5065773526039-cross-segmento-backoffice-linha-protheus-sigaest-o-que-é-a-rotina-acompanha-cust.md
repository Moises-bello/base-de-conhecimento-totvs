---
article_id: 5065773526039
category: ACOMPANHA CUSTOS - JORNADA DE FECHAMENTO (NOVO)
content_hash: f2a45353e8c5b54eceeff0e913b09ea429879556a626e47ae3443b60ae7ad816
fetched_at: '2026-06-28T22:38:48.266628+00:00'
product: protheus
section_id: 5367899706647
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - O que é a rotina Acompanha
  Custos?
type: support-article
updated_at: '2025-11-17T19:50:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5065773526039-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-O-que-%C3%A9-a-rotina-Acompanha-Custos
---

**Dúvida**  
O que é a rotina Acompanha Custos?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33.

**Solução**

**O que é o Acompanha Custos?**

O Acompanha Custos é um painel moderno que irá concentrar todas as informações necessárias **para o acompanhamento dos custos de seu estoque**.

As diversas informações disponibilizadas permitirão a análise da composição do custo dos produtos, sua evolução ao longo do tempo, bem como a criação de alertas para monitoramento dos custos de seus produtos mais relevantes e o **acompanhamento de todo o processo de fechamento de estoque da empresa**.

Apresentamos a nova jornada de Fechamento de Estoque; através de uma interface única, totalmente focada na experiência do usuário, o cliente será conduzido durante seu fechamento de estoque de forma simples, intuitiva e sem a necessidade de realização de configurações ou execução de rotinas adicionais.

**Informações importantes**

O Acompanha Custos necessita de **Lib de 07/01/2021 ou superior**.

**ATENÇÃO**

Para acessar o painel Acompanha Custo, é necessário seguir os seguintes requisitos:

* No dicionário de dados do cliente, deve existir as tabelas: Log de Fechamentos (D3X) e Fechamento Realizado (D3Y).
* Na tabela Parâmetros (SX6) o parâmetro utilizar a execução exclusiva (MV\_CUSTEXC) deve possuir a coluna X6\_CONTEUD='N'
* Necessário cadastrar e habilitar o parâmetro de controle automático de bloqueio de movimentações - [Controle automático de bloqueio de movimentação - MV\_CMDBLQV](https://tdn.totvs.com/x/4zrjIg)   
  Caso apresente algum erro ao iniciar o Acompanha Custo, será necessário aplicar o pacote de atualização.

**Extremamente Importante**

**O Ambiente deve possuir as atualizações mais recentes abaixo.**

* **Atualização Expedição Continua release 12.1.33 para utilização do acompanha custos:** [**Clique Aqui**](https://suporte.totvs.com/portal/p/10098/download#detail/1039086)
* **Possuir a atualização da expedição Continua do Contábil em dia** [**Clique Aqui**](https://tdn.totvs.com/display/public/PROT/Contabilidade+Gerencial)

**Siga o passo a passo abaixo para implantação inicial e utilização do Acompanha Custos.**

**1.** Ajuste os arquivos **appserver.ini**, com a[**Porta Multiprotocolo**](https://tdn.totvs.com/x/jIUoI) e outras chaves necessárias, conforme explanado a seguir.

Insira no **appserver.ini**as chaves abaixo, **independente do tipo de comunicação**utilizado no ambiente (recomendamos a utilização em todos os .ini, pois devido aos balances pode ser que a conexão usual seja destinada a um balance que não possua as chaves por exemplo):

```
[GENERAL]  
App_Environment=ENVIRONMENT  
  
[DRIVERS]  
MultiProtocolPort=1  
  
[HTTPREST]  
Security=1
```

**Caso possua mais de 1 ambiente:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34730239444119)

[**REST MPP (Porta única) - Mais de um ambiente**](https://tdn.totvs.com/x/HwgEN)

**Caso não faça dessa forma, a rotina não ira abrir no formato PO-UI, e rotina que necessitam da chave App\_Environment não vão funcionar.**

**Se incorreto, sera apresentado a seguinte mensagem:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36396578760599)

**2.** Adicione a rotina no Menu do módulo SIGAEST, seguindo os passos abaixo:

1) Acessar o SIGACFG;  
2) Acessar a rotina Ambiente→ Cadastros→ Menus (CFGX013);  
3) Selecionar o módulo de Estoque/Custos;  
4) Selecionar a opção Novo Item;  
Preencher as informações do novo item de menu como indicado no gif abaixo:

![MenuMATA038.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5241834280215)

Agora já possui as configurações iniciais para a rotina Acompanha Custos.

**Para inicialização da rotina**, deve-se seguir o procedimento abaixo, pois é necessário a atualização do dicionário de dados.

**Saiba Mais**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Validação para inicia a rotina Acompanha Custos*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5240908654999)
