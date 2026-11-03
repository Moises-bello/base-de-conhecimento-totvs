---
article_id: 34823839541655
category: Escrita Fiscal - Configurador de Tributos
content_hash: 947afde860a9656f1c25966786a939b2176090d833169d38a196dca571b9f0d7
fetched_at: '2026-06-28T22:39:17.319048+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como calcular
  ICMS Efetivo pelo Configurador de Tributador?
type: support-article
updated_at: '2025-09-10T13:42:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34823839541655-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-ICMS-Efetivo-pelo-Configurador-de-Tributador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34823802661399) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como calcular ICMS Efetivo pelo Configurador de Tributador?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**  
Veja abaixo as devidas configurações para calcular o ICMS Efetivo dentro do Configurador de Tributos

* **Cliente**

Tipo (A1\_TIPO) = Consumidor Final

**TES**  
Deve estar com o CFOP preenchido de acordo com a sua operação.

* **Cadastro do Produto**

NCM e Origem devem estar iguais as informações que for cadastro do Configurado de Tributos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34823802662167)

* **Regra de NCM**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34823839484951)

* **Perfis**

**Perfil do Produto:** Crie um perfil com o cadastro do produto (SB1) que estará utilizando na operação

**Perfil de Operação:** Esse perfil já traz uma listagem de cadastros ao realizar o primeiro acesso na rotina.   
A empresa pode selecionar um perfil já existente ou criar um novo.

**Importante:** o perfil de operação deve contar o mesmo CFOP que esta cadastrado no TES. Caso o TES não seja o mesmo, o calculo não é será apresentado no documento.

**Perfil de Participante:** Vincule o cliente ou fornecedor que será utilizado na operação

**Perfil de Origem/Destino:** Esse perfil já traz uma listagem de cadastros ao realizar o primeiro acesso na rotina.   
A empresa pode selecionar um perfil já existente ou criar um novo.

* **Regra de Base de Calculo**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34823839485975)

* **Regra de Alíquota**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34823839486487)

* **Regra de Escrituração**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34823802669847)

* **Regra de Calculo - Documento Fiscal**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34823839487895)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34823802674583)

* **Pedido de Venda**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34823839491479)

* **Gravação das tabelas**

Seguindo a devida configuração, os campos FT\_BICEFET, FT\_PICEFET e FT\_VICEFET referente ao ICMS Efetivo serão gravados corretamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34823802678167)
