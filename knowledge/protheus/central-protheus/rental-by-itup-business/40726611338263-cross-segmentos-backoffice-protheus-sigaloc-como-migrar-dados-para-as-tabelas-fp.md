---
article_id: 40726611338263
category: Rental by ItUp Business
content_hash: afdcfb467eb2f923d46df2bdb4c3b4dd3b39b66b7f4e024cdb850b3669803b73
fetched_at: '2026-06-28T22:36:20.571164+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Como migrar dados para as
  tabelas FPY e FPZ utilizando Rdmake
type: support-article
updated_at: '2026-05-26T16:58:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40726611338263-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Como-migrar-dados-para-as-tabelas-FPY-e-FPZ-utilizando-Rdmake
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40726606717335) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como utilizar a ferramenta de migração de dados (Rdmake) para as tabelas **FPY** e **FPZ** após a atualização de release e ativação do parâmetro **MV\_LOCBAC**?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - P12.1.2410  
  
**Solução**  
Ao efetuar a atualização do sistema (versões **12.1.2310** ou **superiores**) e utilizar o parâmetro **MV\_LOCBAC** com conteúdo **.T.**, o módulo de Locação de Equipamentos passa a armazenar dados relacionados ao pedido de venda de aluguel nas tabelas **FPY** (dados anteriormente na **SC5**) e **FPZ** (dados anteriormente na **SC6**).

Para manter a integridade das operações de contratos já cadastrados, é imprescindível migrar os dados previamente registrados utilizando um Rdmake específico.

Importante: Ao utilizar **MV\_LOCBAC** = **.T.**, os Pontos de Entrada que conectam o módulo de locação aos demais devem ser "**descompilados**". Se o ambiente possuir Pontos de Entrada compartilhados com outras customizações, é necessário realizar um "**merge**" no código, excluindo apenas as funcionalidades referentes à locação.

Passos:

1. Verifique os **Pontos de Entrada** compilados no RPO. Exclua ou ajuste (retirando o código de Locação) os seguintes pontos: **MS520VLD, M410STTS, SF2520E, A100DEL, MA410DEL, MS520DEL, SF2460I, MT100LOK, A103DEVOL, MT103FIM, MNTA4206, MNTA2952, SD1100I, SF1100E e MNTA400F**.
2. Realize o download do código-fonte do migrador disponibilizado pela TOTVS. O arquivo encontra-se anexo a esta documentação e está salvo com a descrição **"gerafp"**.
3. Compile o código-fonte do migrador no seu ambiente utilizando a IDE oficial (ex: TOTVS Developer Studio / **VS Code**).
4. Acesse o módulo Configurador (**SIGACFG**) e crie um item de menu no módulo Locação de Equipamentos (**SIGALOC**) para chamar a rotina. Informe no campo "**Programa**" a função: **GERAFP**.
5. Acesse o Smartclient com um usuário "**administrador**", entre no módulo Locação de Equipamentos e clique no novo menu criado para o Migrador.
6. Na tela de "**Geração da FPY e FPZ**", o sistema questionará: "**Confirma a importação dos registros?**". Clique em "**Sim**".
7. Aguarde a barra de processamento concluir a leitura e gravação dos registros.
8. Ao término, será exibida uma janela de aviso informando a quantidade de registros gerados e o nome do arquivo de log criado. Clique em "**Fechar**".
9. Acesse a pasta System do Protheus e localize o log gerado (nome semelhante a "**fpy-AAAAMMDD-HHMMSS.txt**") para conferir o detalhamento dos pedidos de venda migrados para as filiais processadas.

**Saiba Mais** [***Migrador de dados - FPY FPZ - Rdmake***](https://tdn.totvs.com/display/public/PROT/Migrador+de+dados+-+FPY+FPZ+-+Rdmake)
