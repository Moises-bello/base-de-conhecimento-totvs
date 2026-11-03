---
article_id: 34358014076567
category: Gestão de Transportes (TMS)
content_hash: 3968a42e38cca136ae3f83a5e252f7964420eda6140602771efd1303c1a16c01
fetched_at: '2026-06-28T22:45:32.564994+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Rejeição 302 - As informações de pagamento
  devem ser informadas para carga lotação
type: support-article
updated_at: '2026-06-24T12:42:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34358014076567-Log%C3%ADstica-Linha-Protheus-TMS-Rejei%C3%A7%C3%A3o-302-As-informa%C3%A7%C3%B5es-de-pagamento-devem-ser-informadas-para-carga-lota%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34358014063895) Tempo aproximado para leitura: **00:05:30 min**  
  
**Dúvida**  
Como resolver a **Rejeição 302 - As informações de pagamento devem ser informadas para carga lotação** na emissão do **MDF-e**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões   
  
**Solução**  
A **Rejeição 302 - As informações de pagamento devem ser informadas para carga lotação** na emissão de **MDF-e** é uma nova rejeição referente a **Nota Técnica 2025.001,** ela ocorre quando o **XML** não possui a *tag* **<infPag> - Informações do pagamento do contrato** e a carga é do tipo lotação (possui um único documento carregado).  
  
A nova regra definida na nota técnica é a seguinte:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34358007023767)

Essa rejeição entrou no ambiente de **homologação em julho de 2025** e em vigor no ambiente de **produção desde 6 de outubro de 2025**.  
  
O TMS liberou a atualização para tratar a montagem da *tag* **<infPag>**, conforme documentação, atualização de pacotes do **TMS** e *schemas* do **TSS** listados em **Saiba mais.**  
  
Com o ambiente devidamente atualizado, a regra para montagem da *tag* para carga lotação é a seguinte:

* No caso de frota própria, a *tag* **<infPag>** é preenchida com os dados do cliente devedor do **CTe** carregado na viagem e com os valores do frete do CTe. Se desejar avaliar, a função que busca os dados do **CTe**contida no rdmake **MDFSEFAZ3** mais recente para preenchimento da *tag* **<infPag>**é a **LoadInfCTe**.
* No caso de frotas de terceiros ou agregados, a *tag* **<infPag>** é preenchida com os dados da filial que está emitindo o **MDF-e**, e os valores são calculados pelo preview do frete a pagar para a viagem. É importante que o Sistema esteja configurado para cálculo de frete a pagar para o fornecedor utilizado na viagem.

**Possíveis situações**  
Caso ocorra a **Rejeição 302** ou alguma falha de *schema* relacionada a *tag* **<infPag>**, verifique as situações mapeadas:

* **XML sem a** ***tag*** **<infPag> preenchida:**
  + Fonte **MDFSEFAZ** ou rdmake **MDFSEFAZ3** desatualizado. Com a versão mais recentes dos fontes, a *tag* **<infPag>** sempre será preenchida, para evitar que a rejeição ocorra. É necessário atualizar seu ambiente com o pacote disponível em **Saiba mais**. Caso utilize o rdmake **MDFSEFAZ3** em seu ambiente, precisa compilar o **MDFSEFAZ3.prw** que está junto com o pacote.
* **Falha de schema:**
  + Falha de schema e não houver as *tags* **<Comp>, <vContrato> e <indPag>** abaixo da *tag* **<infPag>**.   
    Se não houver essas *tags*, é porque o Sistema não encontrou valores de frete a pagar para frota terceira ou agregada. **O Sistema deve estar configurado para cálculo de frete a pagar para o fornecedor.** Para se certificar que o cálculo de frete a pagar para o fornecedor esteja configurado corretamente, realize o seguinte teste: com o preview do contrato carreteiro habilitado, gere um contrato carreteiro para o mesmo fornecedor de **DTR\_CODFOR** e valide se o preview do frete a pagar é exibido com os valores corretamente.
    - Caso não possua nenhum contrato de fornecedor e tabela de frete a pagar e queira fazer um cadastro genérico para ser utilizado no **MDF-e**, pode realizar o cadastro do contrato do fornecedor para o fornecedor genérico preenchido no parâmetro **MV\_FORGEN**.
  + Falha de schema que **não apresenta mensagem ao validar schemas** ou que mostra mensagem relacionada a falta da *tag* **<infBanc>**. Para preencher os dados bancários, o Sistema segue a seguinte regra;
    - Se a viagem possui integração com operadora de frotas:
      * Se for com a Pamcard e a forma de pagamento do saldo do frete for cartão (**DLD\_TIPPAR = 2 - Saldo Frete e DLD\_FORPAG = 1 - Cartão**), a **ANTT** determinou que o número do cartão deve ser preenchido no campo **chave PIX**, então o Sistema preenche o número do cartão na *tag* **<PIX>.**
      * Em outros casos, o Sistema envia o CNPJ da operadora de frota na *tag* **<CNPJIPEF>.**
    - Se a viagem não possui integração com operadora de frotas:
      * O Sistema busca se o proprietário do veículo (**DTR\_CODFOR** e **DTR\_LOJFOR**) possui dados bancários nos campos (**A2\_BANCO** e **A2\_AGENCIA**) para preencher as *tags* **<codBanco>** e **<codAgencia>,** ou **chave PIX** na tabela **F72 - Chaves Pix Fornecedores** relacionados ao cadastro do fornecedor para preencher a *tag* **<PIX>**.
  + Transmissão de **MDF-e** com carga lotação e frota própria sem atualizar os *schemas* do **TSS**. No caso de carga lotação e frota própria, com esta atualização, o Sistema envia a *tag* **<tpComp> - Tipo de componente** com o novo valor **04 - Frete**, e se não atualizar os *schemas*, isso irá gerar uma falha de *schema* por enviar um tipo de componente que não consta nos *schemas* desatualizado.

**Glossário**  
**CNPJ** - Cadastro Nacional da Pessoa Jurídica  
**CT-e** - Conhecimento de Transporte eletrônico  
**MDF-e** - Manifesto de Documentos Fiscais eletrônico  
**PIX**- Pagamento Instantâneo brasileiro  
**TMS** - Transportation Management System  
**TSS** - TOTVS Service SOA  
**XML** - Extensible Markup Language

**Saiba mais**  
Documentação da atualização: [DT 302/Rejeição: As informações de pagamento devem ser informadas para carga lotação](https://tdn.totvs.com/pages/releaseview.action?pageId=969993522)   
Atualização dos RDMAKES: [Logística - Linha Protheus - TMS - RDMAKES para o CTe e MDFe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/24339487959703-Log%C3%ADstica-Linha-Protheus-TMS-RDMAKES-para-o-CTe-e-MDFe)  
Atualização *schemas* **TSS**: <https://suporte.totvs.com/portal/p/10098/download?e=761857>
