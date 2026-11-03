---
content_hash: 7df5eaea79767c0fed59ed945e9092bb553bb2f9aa2393bb595bc0219f94918c
fetched_at: '2026-07-02T19:24:28.816520+00:00'
page_id: '859078120'
product: protheus
source: tdn-tec
title: Application Server - 20.3.2.14
type: documentation
url: https://tdn.totvs.com/display/tec/Application+Server+-+20.3.2.14
version: 14
---

Application Server - 20.3.2.14

# Correções

Validação de patch não acusa fontes mais antigos

Incidente: Quando era enviado um request de validação de patch, sem chave de compilação, estava selecionando o rpo errado para validar os fontes mais antigos.

Solução: Ajuste para pegar o rpo correto para validar o patch.

  

Referente ao chamado: DTAPPSRV-7653

TSS - PDF Corrompido

Incidente: API do s.o. Windows retorna nulo/erro ao executar a função GetDC (erro inesperado), e causa erro na rotina da TMsPrinter.

Solução: Criado um pool de handles para usar esse pool caso ocorra erro na API do Windows.

Referente ao chamado: DTAPPSRV-8089

Correção de funcionamento do Broker Agent

Incidente: Quando um Application Server instanciado pelo Broker Agent era finalizado de maneira forçada (por exemplo, via `Task Manager` do Windows ou `kill` do Linux), o Broker Agent não estava instanciando outro Application Server para atender as regras de escalabilidade.

Solução: Corrigido o funcionamento para instanciar um outro Application Server.

Referente ao chamado: DTAPPSRV-8095

Access Violation - Criação de conector do Smartview

Incidente: Access violation na criação de um conector para o Smartview em ambientes linux.

Correção: Correção na busca de Annotations, em ambiente linux, na execução da rotina de criação de conector para o Smartview.

Referente ao chamado: DTAPPSRV-8056

Access Violation - Acesso URL com path inválido

Incidente: eventual queda do Appserver quando em tentativas de acesso ao REST utilizando URLs com path inválido (http status 404).   
  
Correção: correção efetuada na camada de comunicação, quando a conexão estava sendo fechado simultaneamente ao tratamento do erro de path inválido.

Referente ao chamado: DTAPPSRV-7808

4GL - ERROR - Invalid stack. Check "OPEN WINDOW" commands.

Incidente: Ao utilizar o OPEN WINDOW em 4GL, com o mesmo nome era emitido uma mensagem de erro, porém ao encerrar a janela com CLOSE WINDOW, não era encontrado o nome da janela na lista devido a duplicidade.

Solução: Ajustado lista de janelas para não adicionar nomes duplicados.

Referente ao chamado: DTAPPSRV-7837

# Melhorias

Aumentar resiliência do arquivo LSNUMBER.VAL

Incidente: Corrompimento do arquivo LSNUMBER.VAL quando do encerramento inesperado do Application Server.

Melhoria: No License Server, quando usada a configuração AUTOSAVENUMBER=1, ao gravar uma versão mais atual do arquivo lsnumber.val em disco, a versão anterior do arquivo é renomeada para lsnumber.bak.

Mesmo em caso de uma parada inesperada do sistema operacional, espera-se obter uma resiliência adicional gravando a última e mantendo a penúltima versão do lsnumber.val em disco.

Referente ao chamado: DTAPPSRV-8096
