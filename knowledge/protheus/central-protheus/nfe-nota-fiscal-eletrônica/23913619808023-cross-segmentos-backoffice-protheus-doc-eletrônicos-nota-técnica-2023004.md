---
article_id: 23913619808023
category: NFe - Nota Fiscal Eletrônica
content_hash: e8916eeb2ee6c552fa7829173208135954317be869e149d9457ef73afa335a99
fetched_at: '2026-06-28T22:40:07.091054+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota Técnica 2023.004
type: support-article
updated_at: '2025-06-09T18:55:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23913619808023-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Nota-T%C3%A9cnica-2023-004
---

**Dúvida**  
Quais serão as alterações da Nota Técnica 2023.004 ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos

Cross Segmentos - TSS

**Solução**

Para a adequação à Nota Técnica 2023.004 Versão **1.00, 1.10 e 1.11**.

O prazo previsto para a Nota Técnica 2023.004 **v1.00, 1.10 e 1.11** é:

Ambiente de Homologação (ambiente de teste das empresas): **25/03/2024**

Ambiente de Produção: **01/07/2024**

1. Atualização do ambiente **TSS (repositório e schemas)**

Atualizar o repositório com o último pacote de expedição continua do TSS disponível no link:

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS)

2. Atualizar a pasta **SCHEMAS** presente na estrutura do TSS através do link:

[TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552-TSS-Atualiza%C3%A7%C3%A3o-dos-SCHEMAS)

2. Atualização do **ambiente Protheus:**

Aplicar o Pacote Acumulado Documentos eletrônicos:  
[Clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=525010692)

Compilar **RDMAKE NFESEFAZ, DANFEII e DANFEIII** (se emitir NF-e) presente no link abaixo:

[Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1152113)

**Saiba mais:**  
*Lembrando que RDMAKE não possui Release sendo assim, pode ser aplicada em qualquer uma todos os pacotes.*

Adequado o ERP Protheus para incorporação das novas tags disponibilizadas na NT 2023.004 versões 1.00, 1.10 e 1.11. Desta forma ao transmitir um documento eletrônico NF-e ou NFC-e via ERP Protheus, o XML a ser integrado com a SEFAZ esteja nos conformes da legislação.

Nesta solução estão associados os ajustes referente a montagem do XML a ser enviado à SEFAZ, onde foram tratadas as seguintes tags:

1. **<DI><CPF>** : CPF do adquirente ou do encomendante.

![](https://tdn.totvs.com/download/attachments/832657483/image-2024-4-17_17-6-6.png?version=1&modificationDate=1713384366523&api=v2)

2. **<DI><CNPJ>** : CNPJ do adquirente ou do encomendante.

**Obs:** A TAG CPF, é informada apenas através da rotina dos Livros fiscais/Faturamento. O módulo SIGAEIC não usará o campo CPF.

3. **<ICMSXX><indDeduzDeson>** : Indica se o valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd): 0=Valor do ICMS desonerado (vICMSDeson) não deduz do valor do item (vProd) / total da NF-e; 1=Valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd) / total da NF-e.

![](https://tdn.totvs.com/download/attachments/832657483/image-2024-3-18_11-5-41.png?version=1&modificationDate=1710770748030&api=v2)

**Obs**: A TAG indDeduzDeson, é informada apenas quando seu valor é positivo (valor =1) .

4. **<pag><detPag><dPag>** : Data do Pagamento.

![](https://tdn.totvs.com/download/attachments/832657483/image-2024-3-18_11-6-9.png?version=1&modificationDate=1710770776413&api=v2)

5. **<pag><detPag><CNPJPag>** : CNPJ transacional do pagamento - Preencher informando o CNPJ do estabelecimento onde o pagamento foi processado/transacionado/recebido quando a emissão do documento fiscal ocorrer em estabelecimento distinto.

6. **<pag><detPag><UFPag>** : UF do CNPJ do estabelecimento onde o pagamento foi processado/transacionado/recebido.

![](https://tdn.totvs.com/download/attachments/832657483/image-2024-3-18_11-6-26.png?version=1&modificationDate=1710770793270&api=v2)

7. **<pag><detPag><card><CNPJReceb>**: CNPJ do beneficiário do pagamento.

8. **<pag><detPag><card><idTermPag>**: Identificador do terminal de pagamento.

![](https://tdn.totvs.com/download/attachments/832657483/image-2024-3-18_11-6-39.png?version=1&modificationDate=1710770806153&api=v2)

Importante

As tags **<dPag>,<CNPJPag>,<UFPag>,<CNPJReceb>** e **<idTermPag>** são preenchidas com dados provenientes do módulo de Controle de lojas (SIGALOJA).

Documento auxiliar: [NF-e/NFC-e - Nota Técnica 2023.004 - Evento ECONF - Bloco YA](https://tdn.totvs.com/pages/viewpage.action?pageId=822688361)

<https://tdn.totvs.com/pages/releaseview.action?pageId=822688361>

<https://tdn.totvs.com/pages/releaseview.action?pageId=838694446>

**Dica**

*Para a completa implementação da TAG de <DI><CPF> será necessário realizar o seguinte procedimento de atualização do sistema ERP Protheus: [DSERFIS1-34691 DT - MATA926 - Criação do campo CPF do adquirente ou encomendante na CD5](https://tdn.totvs.com/pages/releaseview.action?pageId=825931504)*
