---
article_id: 360055240194
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 4955d593c5529dc3040ed08a0ee93facd7318e9324affce9dbccd56ddd91df8b
fetched_at: '2026-06-28T22:38:57.114355+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310 MATA311 -
  Transferência entre Filiais com códigos de produtos diferentes
type: support-article
updated_at: '2025-03-12T12:25:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055240194-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Transfer%C3%AAncia-entre-Filiais-com-c%C3%B3digos-de-produtos-diferentes
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21661201729815) Tempo aproximado para leitura: **00:03:15 min****

**Instruções sobre como efetuar a Transferência entre Filiais quando produtos Origem e Destino são de códigos diferentes**  
**Melhoria**

Implementada tratativas através do **parâmetro MV\_TRFVLDP** para permitir a Transferência de produtos com **códigos diferentes entre filiais**, onde a ausência do parâmetro ou conteúdo 1 é mantido os tratamentos atuais para produtos com mesmo código e o conteúdo 2, permitirá a transferência de códigos diferentes desde que haja a amarração de produto x fornecedor na filial destino, ou conteúdo 3  permite transferir sem validar o código do produto.

<https://tdn.totvs.com/pages/releaseview.action?pageId=827310547>

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

Para utilizar essa funcionalidade o conteúdo do parâmetro poderá ser utilizado com **1, 2 ou 3**, veja as descrições abaixo:

**- 1 -** Parâmetro ausente ou com conteúdo igual a 1: **Somente produtos com códigos iguais** na filial origem e filial destino serão permitidos na transferência, configuração padrão.

**- 2 -** Poderá ser transferido produtos diferentes **desde que exista a Amarração de Produto X Fornecedor na Filial Destino**, sendo que o Fornecedor será a Filial Origem. Também é necessário indicar no campo A5\_CODPRF o código do produto da Filial Origem. Veja um exemplo no print abaixo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21661171895831)

**- 3 -** Permite que **todas as transferências** de produtos sejam destinadas para códigos diferentes.

Este parâmetro estará disponível a partir da release 12.1.30 e em releases anteriores deverá ser criado manualmente.

Segue passo a passo para a criação do parâmetro, caso necessário:

* Acesse o módulo Configurador (SIGACFG - 99);
* Acesse a rotina de Base de Dados (CFGX031);
* Selecione a opção de Parâmetros;
* Selecione a opção de incluir novo parâmetro:

Informe os seguintes conteúdos nos campos:

 - Nome de Var. : **MV\_TRFVLDP**

 - Tipo : 1 - **Caractere**

 - Cont.Descriç: **1**

**Na Aba de Descrição:**

 - Descrição : Define método de validação de códigos de produtos na transferência entre filiais: 1- Códigos iguais; 2-Produto X Fornecedor; 3- Não valida. 

![mv_trfvldp.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/24478754144535)

Saiba Mais:

[SIGAEST - MATA310 / MATA311 - Como configurar a Transferência entre Filiais (MATA310 / MATA311) no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418209855639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-configurar-a-Transfer%C3%AAncia-entre-Filiais-MATA310-MATA311-no-Protheus?source=search)

[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
