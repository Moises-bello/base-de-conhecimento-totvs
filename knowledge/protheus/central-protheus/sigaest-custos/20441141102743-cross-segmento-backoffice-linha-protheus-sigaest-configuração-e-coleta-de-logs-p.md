---
article_id: 20441141102743
category: SIGAEST - CUSTOS
content_hash: 6112a08f651f6167754ea66cb71ba2ab2f1eba2f9088dcf834d161cf14739595
fetched_at: '2026-06-28T22:39:00.824262+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Configuração e coleta
  de logs para avaliação da performance no recalculo de custo médio
type: support-article
updated_at: '2026-04-14T16:24:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20441141102743-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-e-coleta-de-logs-para-avalia%C3%A7%C3%A3o-da-performance-no-recalculo-de-custo-m%C3%A9dio
---

O artigo orienta sobre como coletar dados para análise de performance na rotina de recálculo do custo médio no TOTVS Protheus, detalhando etapas, parâmetros, anexos necessários para suporte e documentação. Destaca diferenças para ambientes não CLOUD e CLOUD TOTVS, recomenda atualizações, configurações específicas e envio de logs para suporte técnico.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20441167343895) Tempo aproximado para leitura: **00:05:40 min**  
  
**Dúvida**

Problema de performance na execução da rotina de recalculo do custo médio; como coletar dados para analise de performance.  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Análises de performance são complexas pois envolvem uma diversidade grande de fatores e variáveis, distribuídas entre o banco de dados, configurações do ambiente, e o produto em si. Deste modo, separamos alguns processos, para que seja avaliado e coletado algumas informações, para a avaliação do processamento do custo médio, e assim entendermos o que esta sendo causado o em seu ambiente.

Para isso vamos classificar 3 topicos: **Etapas,** **Anexos para o suporte** e **Documentações do processo**

Situações de analise > Tópico:

1. **(Seu Ambiente não é CLOUD TOTVS)**
2. **(Seu Ambiente é CLOUD TOTVS)**

A validação de todo o processo, é necessario ser efetuada junto a um analista de suporte tecnico do cliente, pois existem dados e processos que somente o analista tecnico tem conhecimento devido.

**Etapas**  
**É uma lentidão generalizada? ou ocorre somente para essa rotina?**  
Caso seja generalizado, avaliar o boletim a seguir.  
[Framework - Linha Protheus - FRAME - Lentidão no Protheus 12](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017515552-MP-FRAME-Lentid%C3%A3o-no-Protheus-12) 

**Caso seja somente para a rotina em questão:**

**(Seu Ambiente não é CLOUD TOTVS)**  
**1 -** Processar o arquivo [**Malloc-IO**](https://tdn.totvs.com/display/public/PROT/MallocIO) dentro do ambiente APPSERVER e DBACCESS   
**2 -** Sugerimos fortemente, que o ambiente esteja contemplado das ultimas atualizações, disponibilizadas no portal do cliente. (> [Atualizações do Sistema Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=550332596#OINF0011.2-Atualiza%C3%A7%C3%B5esProtheus-Modulos) <)  
**3 -** Configure o ambiente, de forma exclusiva (solicitar ao seu dpto de TI se necessario).  
**4 -** Configure o **logprofiler** e **dbtrace** para coleta do log de processamento da rotina MATA330 - Recalculo de custo médio.  
**5** **-** Utilizar as procedures referente a rotina de forma que estejam atualizadas. (> [Como atualizar as procedures](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009382821-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-instalar-as-Stored-Procedures-) <)

**6 -** O parametro **MV\_MOEDACM** considera o calculo no padrão para 5 moedas de forma simultanea, caso você não tenha necessidade de calcular moedas estrangeiras, considerar o conteudo do parametro em branco. (> [Sobre o parametro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410094201623-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-Utilizar-e-Calcular-os-Custos-em-Outras-Moedas-Utilizando-o-Parametro-MV-MOEDACM-Custo-M%C3%A9dio-MATA330-) <)

**7 -** Valide a necessidade de usar o parametro **MV\_A330GRV caso esteja ativo,** este parâmetro é recomendado para clientes possuem uma quantidade de registros na tabela SB2 superior a 10 mil registros, **pois ele evita o processamento desnecessário de produtos/armazém obsoletos que não tem necessidade de recalculo.**  
Para uma melhor performance o parâmetro deve estar configurado com o **conteúdo igual a .F. (False).**  
**IMPORTANTE:** Caso utilize os pacotes de stored procedures para execução da rotina é recomendada a reinstalação das SP's após a alteração deste parâmetro, sem esta ação o objetivo de melhora no desempenho não será atingido caso você tenha feito a alteração do mesmo.

Bem como deve ser feita a coleta do TRACE do banco, e a avaliação do seu DBA informando se existem ou não pontos de melhoria durante a analise das consultas executadas na camada da sua base de dados.

**8 -** Processe a rotina após todas as etapas acima terem sido efetuadas, e aguarde até sua finalização.

**Anexos para o suporte (Importante que todos esses itens sejam providenciados para envio em ISSUE de Manutenção do Suporte)**

**Após finalização do processamento da rotina, enviar ao suporte os arquivos:**

- Logprofiler 

- Dbtrace

- Inspetor de objetos

- Log tabela **CV8** em formato .sqlite filtrada pelo campo **CV8\_PROC** = Nome da rotina 

- Print do Malloc-IO

- Enviar os dados da [**Central de Diagnóstico**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33711098138007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-enviar-dados-pela-Central-de-Diagn%C3%B3stico) do ambiente que apresenta a lentidão, Veja [**nessa FAQ**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33711098138007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-enviar-dados-pela-Central-de-Diagn%C3%B3stico) como providenciar esses dados. 

**Documentações do processo**  
Como gerar o **logprofiler e dbtrace** via Appserver.ini:  
[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como habilitar e gerar o LogProfiler?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019902592-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-habilitar-e-gerar-o-LogProfiler-)  
  
 

Como gerar o processamento do **Malloc-IO**  
[How To| Malloc IO Análise de performance do hardware](https://www.youtube.com/watch?v=UeO3VbLw2R8)

**Parametros para avaliação de performance no processamento da rotina:**

MV\_A330GRV, MV\_A330DRV, MV\_CUSTEXC, MV\_M330THR, MV\_MOEDACM, MV\_THRSEQ, MV\_M330JCM, MV\_PRODMOD

**Sobre cada um deles:**

<https://tdn.totvs.com/pages/viewpage.action?pageId=336404235#:~:text=Configura%C3%A7%C3%B5es%20de%20par%C3%A2metro%20SX6>

**(Seu Ambiente é CLOUD TOTVS)**

Informar ao suporte, os dados do ambiente, para possamos solicitar internamente em um ticket junto ao time **CLOUD ATENDIMENTO**, configurações necessarias para avaliação de performance, com anexo do inspetor de objetos do ambiente.

(**ATENÇÃO**: ***O suporte só efetuara a avaliação somente em ambiente de Homologação**, portanto sugerimos que o cenario esteja apresentado em ambiente de homologação, e caso não esteja, deve-se solicitar a replica do ambiente de produção para o ambiente de homologação, de forma que possamos prosseguir com as analises )*

**Ambiente teste deve estar configurado em modo EXCLUSIVO.**

-Nome do ambiente 

-Arquivo Smartclient.ini do ambiente que esta acessando

-Informar qual a "Comunicacao do cliente" esta usando (ex: TCP)  
-ID do ambiente​  
-Nome e código da filial que se encontra com o erro​  
-nome de usuário e senha adm <https://getmypassword.cloudtotvs.com.br/> (sugerimos um usuario para o suporte, informe a senha desse usuario no link, não é para gerar uma senha exemplo de como colocar abaixo, para termos a senha do USUARIO de acesso ao ambiente)

**IMPORTANTE**  
Cada questão contida no formulário e logs solicitados foram elaborados para agilizar e prover uma análise assertiva e criteriosa em ocorrências de performance, por isso, havendo dúvidas, solicite apoio à seu time de TI para que todas as questões sejam devidamente preenchidas. Elas são essenciais para continuidade neste atendimento.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
