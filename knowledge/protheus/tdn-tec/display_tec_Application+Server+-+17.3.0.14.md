---
content_hash: e610260031644d4db2a84cb99c43ee938285ed6cd8a5af7fc646080a94a767cd
fetched_at: '2026-07-02T19:24:25.831509+00:00'
page_id: '513414422'
product: protheus
source: tdn-tec
title: Application Server - 17.3.0.14
type: documentation
url: https://tdn.totvs.com/display/tec/Application+Server+-+17.3.0.14
version: 3
---

# RedNÃO EXPEDIDO

# Implementação

 Implementar suporte a múltiplos RPOs

Permitir que seja utilizado um repositório auxiliar, um RPO customizado com programas completos ou funções especificas, permitindo a rápida customização de um determinado ambiente com um "pacote" completo (RPO Customizado), sem precisar aplicar o pacote no repositório padrão.  
  
Para maiores informações, acesse: <http://tdn.totvs.com/display/tec/RPOs+Multiplos>

Referente ao chamado: TTEC-3190

# Melhoria

 Permitir desabilitar o parâmetro X-Frame-Options dinamicamente

Referente ao chamado: TTEC-3241

 Arquivo de INI auxiliar para configurações especificas

Criado uma chave de ini para ser colocado na seção "General" chamada IniCustomization. Para maiores informações acesse: <http://tdn.totvs.com/display/tec/IniCustomization>

Referente ao chamado: TTEC-3280

# Correção

GetServerIP retornado IP "vazio"

Referente ao chamado: TTEC-3181

 HTTPOST - Retorno 401

Incidente: Função HttpPost não retorna erro 401.  
  
Solução: Ajustado método para que erro seja retornado corretamente.

Referente ao chamado: TTEC-3279

 Implementar a atualização automática do SmartClient MacOSX

Incidente:  
Implementar a atualização automática do SmartClient rodando em sistema operacional MacOSX.  
  
Solução:  
Implementada a funcionalidade e documentada as instruções de utilização no TDN na página da seção "UPDATE".  
Esta funcionalidade exige que o AppServer tenha versão mínima 17.3.0.14 e o SmartClient versão mínima 17.3.0.9.

Referente ao chamado: TTEC-3292
