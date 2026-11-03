---
content_hash: b8bc8a5897956abfc2ec1b535dd1a8df51fbf47c55048ca957a433d98be49787
fetched_at: '2026-06-29T00:12:13.928283+00:00'
page_id: '960999204'
product: rm
source: tdn-rm
title: DT - Integração RM X Ahgora - Opção para Não Enviar Funcionários que Não Batem
  Ponto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=960999204
version: 15
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração RM x Ahgora – Opção para Não Enviar Funcionários que Não Batem Ponto |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito **relacionado) :** | [DRHROTRM-13291](https://jiraproducao.totvs.com.br/browse/DRHROTRM-13291) |

## **02. LIBERAÇÃO**

  Lembrando que, será a partir dos patches:

* 12.1.2410.261
* 12.1.2502.164
* 12.1.2506.108 e superiores

## **03. SITUAÇÃO/REQUISITO**

Evoluir a integração entre o TOTVS Folha de Pagamento e o Ponto Web da Ahgora, incluindo opção de não enviar os funcionários que não realizam a marcação de ponto. Essa melhoria facilitará a gestão e o acompanhamento da integração, proporcionando mais agilidade e clareza para os usuários, especialmente em ambientes com grande volume de colaboradores.

## **04. SOLUÇÃO**

Para atender aos diversos cenários de envio de funcionários nos clientes que utilizam a integração entre a Folha de Pagamento e o Ponto Web da Ahgora, implementamos novas opções no parametrizador.

Para realizar a parametrização, basta acessar o menu Configurações | Parametrizador | Integrações | Ahgora | Aba Gerais | Aba Gerar funcionários.

Disponibilizamos três opções para que os usuários possam escolher quais funcionários terão gatilhos gerados e serão integrados:

**Gerar todos os funcionários, incluindo líderes e líderes externos, independentemente de baterem ponto:**  
Ao selecionar esta opção, serão gerados gatilhos para todos os colaboradores, sem exceção, que batem ou não ponto.

**Gerar somente funcionários e líderes que batem ponto:**  
Essa opção gera gatilhos apenas para funcionários e líderes (funcionários) que realizam marcação de ponto.

**Gerar funcionários e líderes que batem ponto, além dos líderes que não batem ponto:**  
Com essa opção, serão gerados gatilhos para todos os funcionários e líderes que batem ponto.

**⚠️ ATENÇÃO:**

* + - Esses parâmetros estão disponíveis a partir dos patches mencionados no [DT - Integração RM x Ahgora – Opção para Não Enviar Funcionários que Não Batem Ponto](https://tdn.totvs.com/pages/viewpage.action?pageId=960999204)
    - A identificação de colaboradores que batem ponto ou não será realizada por meio da marcação disponível no menu Menu Funcionários | Aba Registro | Aba Ahgora.
    - A opção **"Integrar todos os colaboradores: Gerar todos os funcionários, incluindo líderes, que batem ou não ponto"** será definida como opção padrão (default) no sistema.

Veja print abaixo demonstrando a tela:

false⚠️ ATENÇÃO:

* A identificação de colaboradores que batem ponto ou não será realizada por meio da marcação disponível em Funcionários | Aba Registro | Aba Ahgora.
* A opção **"Integrar todos os colaboradores: Gerar todos os funcionários, incluindo líderes, que batem ou não ponto"** será definida comoopção padrão (default) no sistema.

## **05. DEMAIS INFORMAÇÕES**

[Integração RM X Ahgora](https://tdn.totvs.com.br/pages/releaseview.action?pageId=877866931)
