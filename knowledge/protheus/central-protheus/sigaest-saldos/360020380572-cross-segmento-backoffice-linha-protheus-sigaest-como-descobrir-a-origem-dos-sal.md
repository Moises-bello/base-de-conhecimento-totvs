---
article_id: 360020380572
category: SIGAEST - SALDOS
content_hash: 0195d27d230a1498b321a585f1385764f9aa778988d26e6c7ce44546d2f6e3f7
fetched_at: '2026-06-28T22:39:14.771771+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como descobrir a origem
  dos saldos na consulta com comando [F4] no Produto?
type: support-article
updated_at: '2026-02-09T12:29:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto
---

O artigo aborda como utilizar a tecla F4 no sistema TOTVS Backoffice (Linha Protheus) para acessar a tela de "Saldos em Estoque" no cadastro de produtos. Explica a importância do parâmetro MV\_TPSALDO para interpretar corretamente a "Quantidade disponível". Além disso, descreve como realizar essa consulta em sistemas MacOS, fornecendo instruções sobre o uso de teclas de função. O texto detalha também os diferentes campos que podem ser visualizados ao pressionar F4, como "Saldo Atual", "Quantidade de Pedido de Vendas", e outros, oferecendo links para relatórios e documentação adicionais para conferência e validação dos saldos.

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30944028367127)*** Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**  
O que quer dizer cada campo ao pressionar a ***tecla F4*** e apresenta a tela de ***Saldos em Estoque*** no Cadastro de Produtos / Saldo Atual / campo **"Quantidade"** ou no campo **"Código"** de algumas rotinas do Estoque?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
Ao selecionarmos um produto e **teclarmos “F4”** temos várias informações úteis que nos ajudam a entender melhor o saldo do produto, neste artigo iremos detalhar cada campo da consulta.

Lembrando que para uma correta interpretação do cálculo da **"Quantidade disponível"**, deve-se atentar ao parâmetro **MV\_TPSALDO**. Nas nossas demonstrações, utilizaremos o parâmetro **MV\_TPSALDO = Q**. Para maiores detalhes deste parâmetro, segue abaixo o link:

[**Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Utilização do parâmetro MV\_TPSALDO**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013215531-MP-SIGAEST-Utiliza%C3%A7%C3%A3o-do-par%C3%A2metro-SX6-MV-TPSALDO?source=search)

### **Como realizar a consulta do F4 em sistema MacOs?**

**1. Pressionar Fn + F4:**  
Se o seu teclado tem a tecla Fn, pressione-a simultaneamente com a tecla F4 para ativar a função padrão associada a F4, que pode ser o Launchpad ou outra função dependendo do aplicativo.

**2. Ativar teclas de função padrão:**  
Se você usa frequentemente as teclas de função e quer que elas funcionem como teclas de função padrão (sem precisar pressionar Fn), você pode ativar essa opção nas configurações do teclado. Vá em "Preferências do Sistema" > "Teclado" > "Atalhos" > "Teclas de função" e marque a opção "Usar teclas F1, F2, etc. como teclas de função padrão".

**3. Usar tecla F4 na Touch Bar:**  
Se o seu MacBook tem Touch Bar, pressione e segure a tecla Fn para exibir as teclas de função na Touch Bar e, em seguida, pressione a tecla F4.

**Tópicos**

1. [Tela de consulta F4](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto#:~:text=1%2D-,TELA%20DA%20CONSULTA%20F4,-2%20%2D%20Saldo)
2. [Saldo Atual (B2\_QATU)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto#:~:text=%C2%A02%20%2D-,Saldo%20atual%20(B2_QATU),-%3A%20O%20relat%C3%B3rio)
3. [Quantidade de Pedido de Vendas (B2\_QPEDVEN)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto#:~:text=3%20%2D-,Quantidade%20de%20Pedido%20de%20Vendas%20(B2_QPEDVEN),-%3A%20quando%20existe)
4. [Quantidade empenhada SA (B2\_QEMPSA)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto#:~:text=4%20%2D-,Quantidade%20empenhada%20SA%20(B2_QEMPSA),-%3A%20Solicita%C3%A7%C3%B5es%20ao)
5. [Quantidade nossa em poder de terceiros (B2\_QNPT)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto#:~:text=5%20%2D-,Quantidade%20nossa%20em%20poder%20de%20terceiros%20(B2_QNPT),-%3A%20podemos%20utilizar)
6. [Quantidade de terceiros em nosso poder (B2\_QTNP)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto#:~:text=6%20%2D-,Quantidade%20de%20terceiros%20em%20nosso%20poder%20(B2_QTNP),-%3A%20Trata%2Dse)
7. [Saldo de terceiros quando a TES não controla estoque (B2\_QTER)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto#:~:text=7%20%2D-,Saldo%20de%20terceiros%20quando%20a%20TES%20n%C3%A3o%20controla%20estoque%20(B2_QTER),-%3A%20Podemos%20utilizar)
8. [Quantidade empenho NF (B2\_QEMPN)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto#:~:text=8%20%2D-,Quantidade%20empenho%20NF%20(B2_QEMPN),-%3A%20Pedido%20de)
9. [Quantidade empenhada (B2\_QEMP)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto#:~:text=9%20%2D-,Quantidade%20empenhada%20(B2_QEMP),-%3A%20Empenhos%20a)
10. [Quantidade de entrada prevista(B2\_SALPEDI)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto#:~:text=10%20%2D-,Quantidade%20de%20entrada%20prevista(B2_SALPEDI),-%3A%20Trata%2Dse)
11. [Quantidade reservada (B2\_RESERVA)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto#:~:text=11%20%2D-,Quantidade%20reservada%20(B2_RESERVA),-%3A%20Ocorre%20quando)
12. [Quantidade a endereçar (B2\_QACLASS)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto#:~:text=12%20%2D-,Quantidade%20a%20endere%C3%A7ar%20(B2_QACLASS),-%3A%20Aplica%2Dse)
13. [Empenhos previstos (B2\_QEMPPRE)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto#:~:text=13%20%2D-,Empenhos%20previstos%20(B2_QEMPPRE),-%3A%20Trata%2Dse)

**Sessões para validação dos saldos**

**1- TELA DA CONSULTA F4**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13440439983255)

**2 - S****aldo atual (B2\_QATU):** O relatório para conferência é o MATR260, segue o exemplo abaixo.

![SALDO_ATUAL.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016602571)

**3 - Quantidade de Pedido de Vendas (B2\_QPEDVEN):** quando existe Pedido de Venda ainda não liberado. Para conferência, pode ser utilizado o relatório MATR700 conforme imagem abaixo:

![QTD_PEVEN.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016550112)

**4 - Quantidade empenhada SA (B2\_QEMPSA):** Solicitações ao armazém ainda "não baixadas". Pode ser utilizado o relatório MATR105 para comparação do saldo, exemplo na imagem abaixo:

![SOL_ARM.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016602791)

**5 - Quantidade nossa em poder de terceiros (B2\_QNPT)**: podemos utilizar o relatório MATR480 para conferirmos as quantidades conforme imagem abaixo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099191394)

**6 - Quantidade de terceiros em nosso poder (B2\_QTNP):** Trata-se da quantidade de produtos terceiros que está em nosso poder. Pode ser comparada com o relatório MATR480.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101422153)

**7 - Saldo de terceiros quando a TES não controla estoque (B2\_QTER):** Podemos utilizar o relatório MATR480 para conferência, porém neste caso constam tanto envio quanto recebimento de produtos que controlam terceiro porém a TES não atualiza estoque.

![PODE3_TES_N_ATU_EST.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016550512)

**8 - Quantidade empenho NF (B2\_QEMPN):** Pedido de venda que gerou OP **(OP's por venda)** Podemos conferir através do relatório MATR850 conforme imagem abaixo.

![GER_PO_PEVEN.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016602991)

**9 - Quantidade empenhada (B2\_QEMP):** Empenhos a partir de OP (MATA381), Lote vencido (tabela SDD -  Conferência através do relatório MATR425) / MATA275 - Bloqueio de Lote ou também quando existe Solicitação de Transferência entre Filiais (via MATA311) ainda não efetivada. Bastando verificar em qual dos critérios o produto se encontra.

![EMP_OP.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016550692)

**10 - Quantidade de entrada prevista(B2\_SALPEDI):** Trata-se da quantidade prevista por pedido de compras, solicitação de compras, documento de entrada com entrega futura (DHQ) e/ou transferências entre filiais ou entre Armazém pela rotina MATA311 e OP (Ordem de produção) em aberto. Os relatórios MATR440/MATR290 servem para conferência.

***Importante:*** Caso o campo B2\_SALPEDI não exibir alguma Solicitação de Compras no cálculo, verifique se o parâmetro MV\_SCSLDBL esta habilitado. [**Clique aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011683932-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Par%C3%A2metro-MV-SCSLDBL-Atualizar-Quantidade-Entrada-Prevista-do-Produto-ao-liberar-Solicita%C3%A7%C3%A3o-de-Compras) e veja a FAQ sobre esse parâmetro.

![QTD_ENTPREV.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016550872)

**11 - Quantidade reservada (B2\_RESERVA):** Ocorre quando existe Pedido de Venda liberado, porém ainda não faturado. Também há outras hipoteses que contemplam a montagem da Reserva. Consulte esta documentação para obter mais detalhes [**clicando aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13412918250263-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-localizar-e-estornar-o-saldo-do-campo-Qtd-Reserva-B2-RESERVA-de-um-produto) Os relatórios para conferência destes saldos são: MATR700/MATR680

![QTD_RESERV.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016603251)

**12 - Quantidade a endereçar (B2\_QACLASS):** Aplica-se para produtos que utilizam controle de localização e ainda não foram endereçados (Tabela SDA). O relatório para conferência é o MATR245.

![QTD_ENDER.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016551032)

**13 - Empenhos previstos (B2\_QEMPPRE):** Trata-se da quantidade de empenho de OP's previstas. Relatórios MATR290/MATR875.

![OP_PREV.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016603291)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Saldos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033462-SIGAEST-SALDOS)
