---
article_id: 16506619056279
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: c812b8391cc222c66ea06eb33957cbd501990365ea500d0825a3c11e03539a87
fetched_at: '2026-06-28T22:37:55.229005+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmento Protheus - Backoffice Linha Protheus - SIGAFIN - FINA710 - Como
  ajustar a informaçao de clientes no Boleto gerado via API
type: support-article
updated_at: '2023-08-03T17:52:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16506619056279-Cross-Segmento-Protheus-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Como-ajustar-a-informa%C3%A7ao-de-clientes-no-Boleto-gerado-via-API
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16506634736279) Tempo aproximado para leitura: **00:10:00 min** **Dúvida**Como ajustar a informação de clientes no Boleto gerado via API?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16506155392151)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.33  
  
**Solução**  
1- Na rotina Novo Gestor Financeiro (FINA710 ) em Comunicação Online -> Configuração de Contas

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/16506192843543)**2 - Editar o Banco que será utilizado para a transmissão via API de boletos (FINA713).  
3 - Na opção de Pagador, é demonstrado os campos da SA1 - Cliente (MATA070) que serão impressos no Boleto gerado pelo transmissão e enviado ao cliente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16512553293335)  
  
Os campos do layout devem estar preenchidos na rotina Clientes (MATA070), para gravar a informação no JSON enviado e gerar o borderô com a informação correta.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16506276801047)  
  
**Relação de campos**  
Nome

```
A1_NOME   Nome do cliente  
A1_NREDUZ N Fantasia Nome Reduzido do cliente
```

CEP

```
A1_CEP  CEP Cod Enderecamento Postal  
A1_CEPC Cep de Cobr. Cep de Cobranca  
A1_CEPE Cep Entr Cep de Entrega
```

Endereço

```
A1_END    Endereco Endereco do cliente  
A1_ENDCOB End.Cobranca End.de cobr. do cliente  
A1_ENDENT End.Entrega End.de entr. do cliente
```

Bairro

```
A1_BAIRRO  Bairro Bairro do cliente  
A1_BAIRROC Bairro Cob Bairro de cobranca  
A1_BAIRROE Bairro Entr. Bairro de Entrega
```

Município

```
A1_MUN  Municipio Municipio do cliente  
A1_MUNC Mun. Cobr. Municipio de Cobranca  
A1_MUNE Mun. entr Municipio de Entrega
```

Estado

```
A1_EST  Estado Estado do cliente  
A1_ESTC Uf de Cobr. Uf de Cobranca  
A1_ESTE Uf Entr Estado de Entrega
```

**Observação**: Alguns bancos não aceitam caracteres especiais nas informações de Pagador ou mensagens adicionais de cobranças, caso possua caracteres especiais nas informações de cliente e mensagens adicionais no boleto, utilize a função **FWNOACCENT** no layout de configuração.  
Exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16506510844823)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16506496411799)  
  
**Saiba mais****[Contas a receber (Comunicação bancária online)](https://tdn.totvs.com/pages/viewpage.action?pageId=612548392)****[Configuração de Contas (Pagar e Receber) - FINA710](https://tdn.totvs.com/pages/viewpage.action?pageId=736963446)****[Webinar TOTVS|MP-SIGAFIN FINA713 Funcionamento Novo Boleto Online #TOTVS BackOffice Linha Protheus](https://www.youtube.com/watch?v=W3Mj4x1vVAE&t=831s&ab_channel=TOTVSSolu%C3%A7%C3%B5es)  
[FwNoAccent](https://tdn.totvs.com/display/public/framework/FwNoAccent)**
