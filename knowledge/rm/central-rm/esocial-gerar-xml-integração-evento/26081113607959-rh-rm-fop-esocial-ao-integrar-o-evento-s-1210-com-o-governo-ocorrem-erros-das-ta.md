---
article_id: 26081113607959
category: eSocial - Gerar XML/ Integração Evento
content_hash: e1e03a4d794a9ea3fc7a55a82db5cfbe299578fd2fcf81a25aee4c2a0c406180
fetched_at: '2026-06-28T22:47:11.984524+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Ao integrar o evento S-1210 com o governo ocorrem
  erros das tags nifBenef e frmTribut do grupo infoPgtoExt
type: support-article
updated_at: '2026-03-12T00:07:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26081113607959-RH-RM-FOP-eSocial-Ao-integrar-o-evento-S-1210-com-o-governo-ocorrem-erros-das-tags-nifBenef-e-frmTribut-do-grupo-infoPgtoExt
---

Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Ao integrar o evento S-1210 com o governo ocorre os erros **- O campo 'nifBenef' do registro 'infoPgtoExt' é obrigatório e não está preenchido; - O campo 'frmTribut' do registro 'infoPgtoExt' é obrigatório e não está preenchido; - Erro na validação do campo 'frmTribut': Valores Válidos: 10, 11, 12, 13, 30, 40, 41, 42, 43, 44, 50.**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - À partir das versões 12.1.2310.229, 12.1.2402.174, 12.1.2406.105 e Superiores.

**Causa**  
O erro ocorre quando faltam Informações complementares relativas a pagamentos a residente fiscal no exterior.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30433622314007)

**Solução**  
Para solucionar o erro é necessário conferir as parametrizações de cadastro do Autônomos Residentes no Exterior.

**- Folha de Pagamento**  
1. Identifique o cadastro do funcionário desejado e acesse **Administração de pessoal| Funcionários** **Anexos | Folha de pagamento | Dados do Residente ou Domiciliado no Exterior** :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26081097092631)

2. Realize o preenchimento dos campos conforme o cenário do funcionário;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26081113595543)

**- Gestão Financeira**

1. Acesse o menu **Administração de Pessoal | Cliente e Fornecedor | Aba Identificação** e preencha as informações do endereço na aba Principal, conforme demonstrado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26081113598615)

2. Acesse o menu **Administração de Pessoal | Cliente e Fornecedor | Aba Tributos** e preencha os campos: **Situação do NIF** e **Forma de Tributação**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26081113599255)

**Importante**  
Necessário conferir se a codificação do País consta conforme [**Tabela 06 - Países do eSocial**](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.3/tabelas.html#06)e se foi realizado a configuração de endereço, mesmo quando o país for Brasil. Para mais informações [**CLIQUE AQU**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007501531-RH-RM-FOP-eSocial-Classifica%C3%A7%C3%A3o-de-pa%C3%ADses-conforme-layout-do-eSocial)**I**.

**Saiba mais**  
Para mais informações acesse:   
- [Evento S-1210](https://tdn.totvs.com/display/public/LRM/Evento+S-1210)  
- [Pagamentos a Residentes ou Domiciliados no Exterior](https://tdn.totvs.com/display/public/LRM/FOP_0005_Pagamentos+a+Residentes+ou+Domiciliados+no+Exterior)  
- [Como o governo valida o S-1210 para identificação do Código de Receita relativo ao IRRF de Autônomos Residentes no Exterior - 047301](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17176376128663)
