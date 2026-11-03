---
article_id: 360018448392
category: RH - Folha de Pagamento
content_hash: e6c1c27956e8dc8512873119e01e4eec6a93f8c216407753fc119ba9a34b5a1b
fetched_at: '2026-06-28T22:44:13.475638+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como executar cálculos da folha de pagamento sem
  customizações (mnemônicos, roteiros, fórmulas e pontos de entrada)
type: support-article
updated_at: '2024-09-12T21:30:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018448392-RH-Linha-Protheus-GPE-Como-executar-c%C3%A1lculos-da-folha-de-pagamento-sem-customiza%C3%A7%C3%B5es-mnem%C3%B4nicos-roteiros-f%C3%B3rmulas-e-pontos-de-entrada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26337013842455)** Tempo aproximado para leitura:**00:03:00 min**

**Dúvida**Como executar cálculos da folha de pagamento sem customizações (mnemônicos, roteiros, fórmulas e pontos de entrada)?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**1. Renomeie a pasta que contém o **repositório de fórmulas (rpofrm),** que fica no diretório do RPO do Protheus (ele é gerado a partir das fórmulas e roteiros do SIGAGPE);

2. Renomeie as tabelas de fórmulas e roteiros, para que o sistema recrie no padrão:

-SRY;  
-SRM;  
-RCA;  
-RC2;  
-RC3;

Acesse o **Configurador (SIGACFG)**, entre em Base de Dados> Dicionários> Base de Dados. Selecione no canto superior esquerdo Dicionário de Dados e depois selecione o ícone com o símbolo de lupa;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014191932)

Será apresentada a tela abaixo. No campo de pesquisa, digite SRY e clique em Buscar. Depois selecione o ícone Editar:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014192551)

No exemplo abaixo, a tabela SRY possui o nome SRYT10, altere para um nome que não exista em seu ambiente, SRYT10\_T por exemplo:**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014193071)**

Após a alteração, o campo Nome será alterado como SRYT10\_T. Clique em Confirmar:**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014193151)**

Será apresentado o *browse* novamente. Clique no ícone com desenho Disquete. Será aberta uma nova janela, clique em Avançar em todas as janelas que forem mostradas:

**Esta ação depende de acesso exclusivo:**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014193191)

Será apresentada a janela abaixo ao fim do processamento. Verifique se será apresentada a mensagem: **Atualização finalizada com sucesso** e **Finalize**.**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014193211)**Após a execução do processo acima com todas as tabelas citadas, acesse o sistema para que as mesmas sejam recriadas, nesta ordem:

* Atualizações - Def. de Cálculo - Mnemônicos
* Atualizações - Def. de Cálculo - Fórmulas
* Atualizações - Def. de Cálculo - Roteiros de Cálculo

3. Desabilite os pontos de entrada do sistema através da chave IXBLOG=NORUN no appserver.ini, mais detalhes em<http://tdn.totvs.com/display/public/PROT/Chave+IXBLOG>

**ATENÇÃO:** Este procedimento desabilitará os pontos de entrada de todos os módulos, por isso é **imprescindível a execução de todos os processos mencionados neste artigo em ambiente de testes.**

**Observações Importantes:**Após a realização dos testes e análise dos cálculos, retornar os nomes das tabelas e pastas ao originais e desativar a chave IXBLOG.  
  
**Saiba Mais:**  
Configuração do Repositório de Fórmulas para ambientes com Balance (balanceamento de carga): <http://tdn.totvs.com/pages/viewpage.action?pageId=208345362>  
[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
