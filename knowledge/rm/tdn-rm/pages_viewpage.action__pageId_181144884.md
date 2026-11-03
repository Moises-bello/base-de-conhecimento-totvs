---
content_hash: 16f91c1243a34d8f19d26486dbfabe97f79f8e79a5d8a46718e811fd5aac9420
fetched_at: '2026-06-29T00:05:57.681943+00:00'
page_id: '181144884'
product: rm
source: tdn-rm
title: Bloqueio do Sistema X Desconexão Automática
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=181144884
version: 49
---

# Índice:

---

.\*ndice:

---

falseAtenção

⚠️ A partir da versão **12.1.2402** a detecção de ausência também considerará o tempo que o RM está em segundo plano.

# Objetivo

---

Esclarecer as diferenças entre as configurações “Tempo espera (min) p/ lock (necessário logoff)” e “Tempo para desconexão automática (min)”.

Obs.: Configurações validas somente para o uso do sistema através da MDI.

# Requisitos

---

| Linha de Software | Versão | Data de Liberação | Observação |
| --- | --- | --- | --- |
| **RM** | 12.01.01 e/ou posteriores | Outubro/2014 | Para os requisitos de software deve-se consultar a portabilidade RM: [Portabilidade RM 12.01](http://tdn.totvs.com/x/CATaCQ) |

# Como Configurar

---

false.1º Passo:

Faça login no sistema através do RM.exe.

Concluído o login dentre as opções do menu acesse: Sistema > Ambiente > Configurações > Parâmetros > Parâmetros Globais.

2º Passo:

O sistema apresentará as opções de Parâmetros Globais, neste, selecione a guia “Configurações Públicas”.

Nesta visão é possível configurar, **em minutos**, os parâmetros:

Tempo espera (min) p/ lock (necessário logoff) **e/ou** Tempo para desconexão automática (min).

falseObservação:

Os campos "Tempo espera (min) p/ lock (necessário logoff)" e "Tempo para desconexão automática (min)", são limitados para receber no máximo 9.999 minutos.

⚠️ **Atenção:**  Após a configuração dos campos é necessário fazer logout no sistema para que a nova parametrização seja aplicada.

# Usabilidade:

---

false.Tempo espera (min) p/ lock (necessário logoff):

* **Tempo para (min) p/ lock (necessário logoff)****:**

   A opção “Tempo espera (min) p/ lock (necessário logoff)” irá bloquear o sistema sem afetar os processos que estiverem em execução e **não fará liberação** das licenças que estão em uso por este usuário.

   Para acionarmos a tela de bloqueio definimos um tempo limite (em minutos) de ociosidade do uso do sistema (RM). Completado os minutos configurados surgirá uma tela de bloqueio. O sistema entenderá que o usuário está ausente e por segurança o acesso ao sistema foi bloqueado.

falseObservação:

* Tendo a estação bloqueada os processos uma vez iniciado não serão interrompidos.
* As licenças de uso que estiverem sendo consumidas não serão liberados mesmo com o bloqueio do sistema.
* Diferente do usuário bloqueado, somente usuário com status de supervisor poderá encerrar a conexão bloqueada.
Tempo para desconexão automática (min):

* **Tempo para desconexão automática (min)****:**

   A opção “Tempo para desconexão automática (min)” irá “derrubar” a conexão deste usuário. Os processos que estiverem em execução serão executados (sendo possível ser visualizado através do Gerenciamento de Jobs). As licenças em uso **serão liberadas**.

   Para acionarmos a tela de desconexão definimos um tempo limite (em minutos) de ociosidade do uso do sistema. Completado os minutos configurados surgirá uma tela informando a desconexão. O sistema entenderá que o usuário está ausente durante o tempo estipulado e encerrará sua conexão.

falseObservação:

* As licenças de uso que estavam sendo consumidas **serão liberadas**.
* Caso o usuário faça login para desbloquear a tela de sessão encerrada, novas licenças serão consumidas. Obs.: Nesta situação haverá a necessidade de licenças disponíveis, caso contrário será apresentada mensagem informando que o número de licenças está excedido.
falseObservação:

* Os processos em execução **não são finalizados** quando ocorre a desconexão automática do sistema, o mesmo será processado e executado normalmente.

---

falsePara maiores informações:

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Segurança

false

**SubProcesso:** Bloqueio do Sistema & Desconexão Automática

falsefalse

**Status:** Finalizado

false

**Data:** 03/08/2016

false

**Autores:**
