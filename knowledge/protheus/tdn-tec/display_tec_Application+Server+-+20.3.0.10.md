---
content_hash: 2174ffbb5d9dd9f125a1d0dd1a04127c30f9bb164c1b5976e1d5946bf52022f0
fetched_at: '2026-07-02T19:24:27.833731+00:00'
page_id: '683369471'
product: protheus
source: tdn-tec
title: Application Server - 20.3.0.10
type: documentation
url: https://tdn.totvs.com/display/tec/Application+Server+-+20.3.0.10
version: 8
---

# Correções

Desfragmentar RPO ou aplicar patchs corrompe o tlpp.rpo caso a chave RPOTLPP esteja configurada

Incidente: A aplicação de Patchs e a Desfragmentação de RPO causa o corrompimento do tlpp.rpo caso a chave RPOTLPP esteja configurada no appserver.ini do ambiente.  
  
Solução: Fizemos um ajuste na camada que trata o tlpp.rpo para evitar que ocorra a manutenção do mesmo, dada a execução do processo de aplicação de patchs e desfragmentação do RPO.

Referente ao chamado: DTAPPSRV-5847

Ao executar o método TMailMessage:SaveAttach Could not create attachment file

Incidente: O método SaveAttach da classe TMailMessage só estava salvando os arquivos em disco após fechar a thread atual, gerando arquivos com tamanho 0 (zero) até o fechamento da thread.  
  
Solução: Corrigido o fechamento dos arquivos realizado pelo método SaveAttach da classe TMailMessage.

Referente ao chamado: DTAPPSRV-5916

Funções que manipulam XML apresentam falha no acesso a arquivos que estão sob um RootPath compartilhado

Incidente: Funções que manipulam XML, em ambientes que utilizam o TOTVS | Application Server Harpia, apresentam erro na leitura de arquivos que estão em um RootPath compartilhado.

Solução: Atualizamos a biblioteca responsável pela integração com XML (libXML2) para uma versão corrigida.

Referente ao chamado: DTAPPSRV-5452

TMailMessage:Clear não limpa o último campo que foi definido

Incidente: O método Clear da TMailMessage não limpa o último campo definido no objeto.  
  
Solução: Corrigido a limpeza feita pelo método Clear da TMailMessage.

Referente ao chamado: DTAPPSRV-5981

# Melhorias

Exibir versão da DBAPI utilizada

Incidente: Não era possível identificar no log qual a versão de biblioteca DBAPI estava ssendo utilizada.  
  
Solução: Exibir a versão da DBAPi no momento da carga da biblioteca.

Referente ao chamado: DTAPPSRV-5961
