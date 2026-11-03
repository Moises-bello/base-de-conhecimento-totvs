---
article_id: 115001427588
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 6a9601fc3915ce8ef59c14597acc650ba8b829359f63614698615e32ddc0a48c
fetched_at: '2026-06-28T22:38:44.188695+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Help A460FLOCK ao selecionar a numeração da Nota de Saída
type: support-article
updated_at: '2026-03-24T12:37:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115001427588-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Help-A460FLOCK-ao-selecionar-a-numera%C3%A7%C3%A3o-da-Nota-de-Sa%C3%ADda
---

**Ocorrência**  
Help A460FLOCK ao selecionar a numeração da Nota de Saída.

**Ambiente**  
Cross Segmentos-TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - todas as versões.

**Causa**  
Essa mensagem pode indicar duas situações:  
 1. Sistema não está encontrando a Série na **SX5** - **Tabela 01** para dar *lock* (reservar a numeração);  
 2. Indica que a Numeração ficou "*lockada*" / reservada (trava de numeração não foi liberada).

**Veja nosso How To a respeito do assunto no YouTube**: [**Help A460FLOCK e o PE CHGX5FIL**](https://youtu.be/Nv_IUYdVoTA)

**Solução**  
1- Para Sistema não está encontrando a Série na **SX5**, segue algumas validações a serem verificadas:

* Compartilhamento da **SX5**: Se o Faturamento é exclusivo (ou seja, registros na **SF2** possuem o campo de Filial preenchido) então, é necessário que o controle de numeração também seja exclusivo. Para o correto compartilhamento há duas opções:
  + **1ª Opção:** **SX5** deve ser exclusiva: Confirme em "*Configurador > Bases de Dados > Dicionário de Dados > SX5*" o modo de compartilhamento da Tabela; e confirme principalmente no *Banco de Dados > Top/Ctree* se os registros da **SX5 Tabela 00** e **Tabela 01** estão ambas com o campo de Filial devidamente preenchidos indicando que o modo de compartilhamento dos registros está adequado.
  + **2ª Opção:** Caso a **SX5** seja compartilhada, utilizar o Ponto de Entrada [CHGX5FIL](https://tdn.totvs.com/x/79ZGJg) para passar o código da Filial logada para a **SX5** a fim de localizar o registro exclusivo da **Tabela 01** (veja aqui  [Exemplo de uso do Ponto](https://tdn.totvs.com/download/attachments/329024579/CHGX5FIL.JPG?version=1&modificationDate=1524657816000&api=v2))
* + **IMPORTANTE**: Não é recomendada a alteração de compartilhamento da SX5 em ambiente Produção já em uso!
* + Validar se os parâmetros **MV\_TPNRNFS** e **MV\_NUMITEN** estão compartilhado para todas as filiais ou exclusivo e criado em todas as filiais, e com conteúdo válido;
  + O parâmetro **MV\_ESPECIE** contém apenas séries já existentes na **SX5 - Tabela 01** ?
  + A série está devidamente criada?
  + Certifique-se de que não há nenhuma instância aberta no Configurador, posicionada na Tabela de controle de numeração, pois se estiver com instância aberta, a Tabela também ficará travada.

2- Indica que a Numeração ficou "*lockada*" / reservada:

* Possui customizações no ambiente? É imprescindível verificar se a ocorrência é reproduzida em ambiente padrão para descartar inconsistências com as customizações.
* Há grande concorrência no faturamento (muitos usuários executando o faturamento simultaneamente)? Recomenda-se que o controle de sequência automática para a numeração do Documento de Saída seja via SD9 (**MV\_TPNRNFS = 3**) para evitar *Lock* de registro por concorrência.

Para mais informações, acesse :<https://tdn.totvs.com/x/GOBgDQ>
