---
article_id: 360056359234
category: MDT - PPP
content_hash: 9c738f81eb3959bf3910f4a0f93f5084750ebe80c607778456975fb797ff2ae7
fetched_at: '2026-06-28T22:44:22.225394+00:00'
product: protheus
section_id: 360010945654
source: central-protheus
title: RH - Linha Protheus - MDT - Como gerar o PPP com o histórico das transferências
  de empresas ou filiais no modulo medicina e segurança do trabalho (SIGAMDT)
type: support-article
updated_at: '2023-12-21T15:05:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056359234-RH-Linha-Protheus-MDT-Como-gerar-o-PPP-com-o-hist%C3%B3rico-das-transfer%C3%AAncias-de-empresas-ou-filiais-no-modulo-medicina-e-seguran%C3%A7a-do-trabalho-SIGAMDT
---

**Dúvida**Como gerar o PPP (Perfil Profissiográfico Previdenciário) com o histórico das transferências de empresas ou filiais no modulo medicina e segurança do trabalho (SIGAMDT)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho  - Todas as versões  
  
**Solução**Esta documentação refere-se exclusivamente a versão do PPP impresso no Módulo de Medicina e Segurança do Trabalho, rotina MDTR700, não tendo nenhuma relação com o PPP Eletrônico maiores informações consulte:  
[RH - Linha Protheus - MDT - Qual diferença entre o PPP impresso no Módulo Medicina MDTR700 e o PPP da Previdência Social consultado através do APP Meu INSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14223826251287)1. Acesse o modulo Configurador (SIGACFG) no caminho: Base de Dados > Base de Dados > Parâmetros e verifique se os parâmetros **MV\_NG2MEMP** (Indica se deve ser exibido na impressão do PPP, o histórico de todas as empresas) e **MV\_NG2MFIL** (Indica se deve ser exibido na impressão do PPP, o histórico de todas as filial) estão com **S**.  
![parametros.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360095659874/parametros.gif)  
  
2. Acesse no modulo SIGAMDT o caminho: atualizações > relatórios > PPP > perfil profissiogr (MDTR700). Defina as perguntas de geração, e na pergunta **Dados Filial** escolha **Todas**  para considerar dados das outras filiais ou **Corrente** para considerar dados da filial atual.

![2020-10-26_10-54-01.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360097958913/2020-10-26_10-54-01.gif) **Observação**Caso não exista a pergunta **Dados Filial** será necessario atualizar a base com o ultimo dicionário diferencial (**UPDDISTR**) do modulo SIGAMDT. Para fazer o download acesse: [MP - MDT - Como fazer o download (baixar) do pacote de expedição continua (acumulado) do modulo medicina e segurança do trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057956773).  
  
3. Exemplo de demonstração:  
a) Note em meu exemplo que tenho transferência entre empresas;  
![transferencia_empresa.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097960013/transferencia_empresa.png)  
b) Agora nesse exemplo demonstro a geração do PPP com o histórico da outra empresa.  
![PPP1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097960253/PPP1.png)![PPP2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095662134/PPP2.png)  
  
**Saiba Mais**  
[Como gerar o PPP (Perfil Profissiográfico Previdenciário) no modulo Medicina (sigamdt), e de onde vem as informações apresentadas no relatório](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050700933)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971487-RH-Medicina-e-Seguran%C3%A7a-do-Trabalho%20)
