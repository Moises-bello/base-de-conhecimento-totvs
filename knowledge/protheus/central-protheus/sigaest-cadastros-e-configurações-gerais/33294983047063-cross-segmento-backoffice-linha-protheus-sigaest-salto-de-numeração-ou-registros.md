---
article_id: 33294983047063
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 589ff6064267af138a2c80bc63897b03ddaeceefdc1313bbc16f7a31707557ed
fetched_at: '2026-06-28T22:39:07.963348+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Salto de numeração
  ou registros duplicados no NUMSEQ
type: support-article
updated_at: '2026-06-03T12:28:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33294983047063-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Salto-de-numera%C3%A7%C3%A3o-ou-registros-duplicados-no-NUMSEQ
---

A partir da Release 2410 do Protheus, o controle do NUMSEQ foi alterado para usar a função NEWPROXNUM via License Server, substituindo o parâmetro MV\_DOCSEQ. Foi criado o campo I\_N\_S\_D\_T\_ nas tabelas SD1, SD2 e SD3 para registrar data e hora da inclusão. Duplicidades ocorrem por intervenções manuais, configuração incorreta da SpecialKey ou customizações antigas. Recomenda-se configurar SpecialKey exclusiva, ativar CheckSpecialKey, evitar uso do MV\_DOCSEQ e, em casos de duplicidade, estornar documentos ou ajustar manualmente com apoio técnico.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33294957854999) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**:  
Como é realizado o controle do NUMSEQ a partir da Release 2410 e como tratar casos de saltos de numeração ou registros duplicados?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.2410 ou Superior.  
  
**Solução**  
A partir da Release 2410, o controle de gravação do NUMSEQ foi alterado para otimizar o desempenho do produto. O sistema descontinuou o uso do parâmetro **MV\_DOCSEQ** e passou a utilizar a função **NEWPROXNUM**, que utiliza o **License Server** para gerar a próxima numeração sequencial.  
  
Para aumentar o rastreio, foi criado o campo **I\_N\_S\_D\_T\_**nas tabelas **SD1 (D1\_NUMSEQ)**, **SD2 (D2\_NUMSEQ)** e **SD3 (D3\_NUMSEQ)**. Este campo, visível apenas via banco de dados, registra a data e hora exata da inclusão do registro.   
  
O License Server define o ponto de partida da numeração através de uma QUERY nas tabelas mencionadas, gravando o registro **@@@SD2** com o maior sequencial encontrado. Problemas de duplicidade geralmente ocorrem por intervenção manual na chave, configuração incorreta da **SpecialKey** entre ambientes ou uso de customizações que ainda apontam para o parâmetro descontinuado.

**Passos:**

1. Verifique se cada ambiente (Produção e Homologação) possui uma **SpecialKey**exclusiva configurada no **AppServer.ini**, funcionando como um cadastro individual no License Server. Detalhes em: [SpecialKey](https://tdn.totvs.com/display/public/framework/SpecialKey)
2. Ative a chave **CheckSpecialKey** na seção **[GENERAL]** do arquivo de configuração do servidor.  
   [SIGAFAT - A chave CheckSpecialKey em seu ambiente está desligada, você deve liga-la para seu uso da seção [GENERAL]](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34672116970519-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-A-chave-CheckSpecialKey-em-seu-ambiente-est%C3%A1-desligada-voc%C3%AA-deve-liga-la-para-seu-uso-da-se%C3%A7%C3%A3o-GENERAL)
3. Certifique-se de que não existam customizações no ambiente que ainda utilizem o parâmetro **MV\_DOCSEQ**. TDN de apoio:[MV\_DOCSEQ](https://tdn.totvs.com/pages/viewpage.action?pageId=840763998)
4. Para correção de base em registros já gravados com duplicidade, a recomendação e avaliar internamente a possibilidade de estornar o documento origem, para que após a configuração da chave **@@@SD2**, no controle de numeração conforme demonstrado no **ponto 2** abaixo, gerar novamente o registro origem sem a repetição do **NUMSEQ**.
5. Em caso de registros já duplicados, efetue a configuração da chave **@@@SD2**, no controle de numeração, segue abaixo procedimento de ajuste, e avalie o estorno dos documentos para nova geração após o ajuste da chave:   
   [Numeração automática pelo License Server](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025501031-Framework-Linha-Protheus-Numera%C3%A7%C3%A3o-autom%C3%A1tica-pelo-License-Server#:~:text=Como%20alterar%20o%20modo%20de,no%20License%20Server%20(padr%C3%A3o).) | [How To - Ajuste de Numeração automática das tabelas](https://www.youtube.com/watch?v=BhEo-9FFUIQ&ab_channel=TOTVSGest%C3%A3o)
6. Se o estorno não for viável, recomenda-se o apoio de um **analista de banco de dados** para saneamento manual dos registros (Caso necessite, recomendamos acionar o Gestor de contas para avaliar a contratação de serviços especializados).
7. Casos de HELP a seguir, podem estar vinculados a registros duplicados que precisam ser reavaliados:

   **IDENTSB6**
8. O campo documento original e/ou serie foi(ram) alterados manualmente para: - Documento XPTO  
   O sistema necessita que esta operação seja realizada através do botão  
   SELECIONAR DOCUMENTO ORGINAL - F7 para atualizar a baixa da tabela SB6

**Saiba mais:**  
[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
