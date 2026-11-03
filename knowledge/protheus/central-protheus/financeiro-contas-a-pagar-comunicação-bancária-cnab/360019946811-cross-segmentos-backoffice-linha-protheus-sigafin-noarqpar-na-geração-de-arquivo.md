---
article_id: 360019946811
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: abb40e244b12ef76b3084b6aa6e82b76e1046cdca931802932b4afb915ed6a2f
fetched_at: '2026-06-28T22:37:55.308828+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN -  NOARQPAR na Geração
  de arquivo CNAB
type: support-article
updated_at: '2025-08-05T18:06:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019946811-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-NOARQPAR-na-Gera%C3%A7%C3%A3o-de-arquivo-CNAB
---

**Ocorrência**No módulo **Financeiro**, ao tentar realizar geração de arquivo CNAB o sistema apresenta HELP: **NOARQPAR**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
 **Causa**  
Este HELP é apresentado por que o nome do layout de configuração no servidor pode estar em letras maiúsculas, conforme testes realizados as mesmas devem estar minúsculas.  
  
**Solução**Para solucionar essa ocorrência, verifique as possibilidades dos **Cenários** abaixo:  
  
**Cenário 1**  
1. Ajustar nome do layout da **configuração CNAB** do Protheus para Letras Minúsculas. (avaliar configuração do servidor Protheus).

2. Verificar o caminho da pasta em que o arquivo de remessa está gravado.

3. Verificar a existência da pasta no caminho indicado para a remessa.

**Cenário****2**

Caso o arquivo de configuração não foi encontrada na pasta *system*.

Basta adicionar um novo arquivo de configuração na pasta *system* que o problema será resolvido.

**Cenário 3**

Caso esteja acessando o sistema por meio do WebApp, siga o procedimento descrito a seguir:

Ao acessar o Protheus via WebApp, clique no ícone de engrenagem para abrir o menu de configurações:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33965500288279)  
  
**2.** Siga até o final da página onde terá o **"Agente Local"** e **marque** o campo onde está a configuração **"Habilita/Desabilita o Agente Local"**:   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33965500293911)

Assim, será possível visualizar ou fazer o download dos arquivos localizado no disco local do computador.

O parâmetro **MV\_RELT** deve estar configurado com o valor **\SPOOL\**.
