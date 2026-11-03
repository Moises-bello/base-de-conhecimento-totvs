---
article_id: 360043361753
category: TAF - REINF
content_hash: 00e670f3b9fb353763bbe4e767953db019b38121bf4d46136204e1556fa47073
fetched_at: '2026-06-28T22:41:33.636433+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como consultar o gerenciador
  de integração
type: support-article
updated_at: '2023-10-08T18:35:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043361753-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-consultar-o-gerenciador-de-integra%C3%A7%C3%A3o
---

**Dúvida**Como consultar o Gerenciador de integração?  
  
**Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 12  
  
**Solução**1) Após o Processamento das suas informações no TAF vá em Miscelânea, Gerenciador de integração.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057703354)

2) Nos campos **Data De** e **Data Até** informe a data em que o processamento foi executado **(TAFAINTEG)** e não o período em que a obrigação fiscal está sendo gerada. O filtro deve ser **Fiscal.**

**Não mudar as outras opções**

![](https://tdn.totvs.com/download/attachments/379308197/image2019-7-31_18-44-50.png?version=1&modificationDate=1564609490600&api=v2)

3) Selecione o Registro com Erro e selecione a opção "expandir".

**Não acessar as outras abas, na análise do layout do TAF, somente visualizamos a aba visão por lote**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058571313)

4) Vá em outras ações, Filtrar.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058571373)

5) Selecione o registro não integrado e "filtre" o registro.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057703594)

6) Valide o registro com erro e selecione a opção Visualizar. (ou selecione duas vezes com o mouse no registro)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058571493)

7) Mensagem de erro na integração.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057703854)

Segue abaixo as documentações dos erros mais comuns e como corrigi-los. Caso o **Gerenciador de Integração** apresente algum erro que não esteja listado abaixo ou que persista após correção, abra uma solicitação para o **Suporte da Totvs** e envie um print do erro e o procedimento que foi efetuado.

Erros de Cadastro:

[MP - FIS - Layout T001AE Código de Receita C0R\_CODREC inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017518832-MP-FIS-Layout-T001AE-C%C3%B3digo-de-Receita-C0R-CODREC-inexistente?source=search)

[MP - FIS - Layout T003 Código de Município C1H\_CODMUN inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018437031-MP-FIS-Layout-T003-C%C3%B3digo-de-Munic%C3%ADpio-C1H-CODMUN-inexistente?source=search)

[MP - FIS - Layout T007 Unidade de Medida C1L\_UM inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022293072-MP-FIS-Layout-T007-Unidade-de-Medida-C1L-UM-inexistente?source=search)

[MP - FIS - Layout T007 Código CEST C1L\_IDCEST inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017515772-MP-FIS-Layout-T007-C%C3%B3digo-CEST-C1L-IDCEST-inexistente?source=search)

[MP - FIS - Layout T007 Código de Serviço C1L\_CODSER inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018249431-MP-FIS-Layout-T007-C%C3%B3digo-de-Servi%C3%A7o-C1L-CODSER-inexistente?source=search)

[MP - FIS - Layout T007 Código de NCM C1L\_CODNCM inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017796591-MP-FIS-Layout-T007-C%C3%B3digo-de-NCM-C1L-CODNCM-inexistente?source=search)

[MP - FIS - Layout T007 Código de origem C30\_ORIGEM inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020990791-MP-FIS-Layout-T007-C%C3%B3digo-de-origem-C30-ORIGEM-inexistente?source=search)

[MP - FIS - Layout T010 Conta Superior C1O\_CTASUP inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018247691-MP-FIS-Layout-T010-Conta-Superior-C1O-CTASUP-inexistente?source=search)

[MP - FIS - Layout T010 Código da Natureza Cta/Grp C1O\_CODNAT inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020556892-MP-FIS-Layout-T010-C%C3%B3digo-da-Natureza-Cta-Grp-C1O-CODNAT-inexistente?source=search)

Erros no movimento: (lembrando que se houver erros na **Integração do Cadastro** e o cadastro não existir no **TAF**, automaticamente, os movimentos também ocorrerão erros na integração, desta maneira **corrija o erro do cadastro e reintegre os movimentos**)

[TAF - FIS - Layout T013 - C20\_CODPAR não existe na base de dados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022473971-TAF-FIS-Layout-T013-C20-CODPAR-n%C3%A3o-existe-na-base-de-dados?source=search)

[MP - FIS - Layout T013 Código de Ajuste C2D\_CODAJ Inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022148372-MP-FIS-Layout-T013-C%C3%B3digo-de-Ajuste-C2D-CODAJ-Inexistente?source=search)

[MP - FIS - Layout T013 GNRE C25\_IDENTI inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018126152-MP-FIS-Layout-T013-GNRE-C25-IDENTI-inexistente?source=search)

[MP - FIS - Layout T013 Conta Contábil C20\_CODCTA inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018252251-MP-FIS-Layout-T013-Conta-Cont%C3%A1bil-C20-CODCTA-inexistente?source=search)

[MP - FIS - Layout T013 Número da Declaração C4F\_NRODE inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018601511-MP-FIS-Layout-T013-N%C3%BAmero-da-Declara%C3%A7%C3%A3o-C4F-NRODE-inexistente?source=search)

[MP - FIS - Layout T013 Código de Serviço C2F\_CODSER inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021431471-MP-FIS-Layout-T013-C%C3%B3digo-de-Servi%C3%A7o-C2F-CODSER-inexistente?source=search)

[MP - FIS - Layout T013 Período Fiscal C2G\_PERFIS Não Informado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022338951-MP-FIS-Layout-T013-Per%C3%ADodo-Fiscal-C2G-PERFIS-N%C3%A3o-Informado?source=search)

[MP - FIS - Layout T013 Identificação do Modelo C20\_CODMOD inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019124371-MP-FIS-Layout-T013-Identifica%C3%A7%C3%A3o-do-Modelo-C20-CODMOD-inexistente?source=search)

[MP - FIS - Layout T013 Centro de Custo C30\_CCUSTO inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017512172-MP-FIS-Layout-T013-Centro-de-Custo-C30-CCUSTO-inexistente?source=search)

[MP - FIS - Layout T013 Campo obrigatório não informado: C28\_INDCAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017557832-MP-FIS-Layout-T013-Campo-obrigat%C3%B3rio-n%C3%A3o-informado-C28-INDCAR?source=search)

[MP - FIS - Layout T020 Código de Ajuste C2T\_CODAJU Inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018491891-MP-FIS-Layout-T020-C%C3%B3digo-de-Ajuste-C2T-CODAJU-Inexistente?source=search)

[MP - FIS - Layout T020 Identificador do Subitem C2T\_IDSUBI Inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018492531-MP-FIS-Layout-T020-Identificador-do-Subitem-C2T-IDSUBI-Inexistente?source=search)

[MP - FIS - Layout T020 Conta Contábil C6Z\_CODCTA inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019817232-MP-FIS-Layout-T020-Conta-Cont%C3%A1bil-C6Z-CODCTA-inexistente?source=search)

[MP - FIS - Layout T021 GNRE C3N\_DOCARR inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018402931-MP-FIS-Layout-T021-GNRE-C3N-DOCARR-inexistente?source=search)

[MP - FIS - Layout T021 Identificador do Subitem C3K\_IDSUBI Inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020264271-MP-FIS-Layout-T021-Identificador-do-Subitem-C3K-IDSUBI-Inexistente?source=search)
