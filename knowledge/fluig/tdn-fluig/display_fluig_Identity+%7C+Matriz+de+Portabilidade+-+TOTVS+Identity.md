---
content_hash: 6c240458e568a31aff83beb93d90425fdad40264bb37f2b371eb7db274a32278
fetched_at: '2026-06-28T21:35:24.787264+00:00'
page_id: '271659128'
product: fluig
source: tdn-fluig
title: Identity | Matriz de Portabilidade - TOTVS Identity
type: documentation
url: https://tdn.totvs.com/display/fluig/Identity+%7C+Matriz+de+Portabilidade+-+TOTVS+Identity
version: 59
---

# Falando de matriz de portabilidade - TOTVS Identity...

---

Na matriz de portabilidade são listados os requisitos necessários para a execução do Identity e aplicativos relacionados, como o SmartSync e Desktop SSO.Fim do suporte ao Internet Explorer

Olá!

Para garantir a evolução contínua e as demandas de segurança do Identity, o suporte ao navegador Internet Explorer 11 **foi descontinuado** desde março de 2020.

A utilização do Internet Explorer 11 para o acesso às aplicações **não será bloqueada** pelo Identity, contudo esse navegador será desconsiderado nas rotinas de desenvolvimento e testes da ferramenta e eventuais falhas de compatibilidade não serão mais atendidas pela equipe de suporte e manutenção do Identity.

Conforme a [Matriz de Portabilidade](https://tdn.totvs.com/x/eDAxE) do Identity, os navegadores homologados para uso serão o **Mozilla Firefox** e o **Google Chrome**.

Recomendamos que seja realizada a migração dos usuários para um dos navegadores mais modernos suportados.

## Execução de aplicativos tipo Plugin

---

Para a utilização do **TOTVS Identity**, recomendamos a utilização de navegadores modernos com suporte a HTML5 e execução de JavaScript habilitada.

| Navegador | Versão Homologada | Observações |
| --- | --- | --- |
| Google Chrome | Versão atual (Evergreen) | Navegador homologado e recomendado. |
| Microsoft Edge | Versão atual (Chromium) | Suportado a partir da engine Chromium (v.79+). |
| Mozilla Firefox | Versão atual (Evergreen) | Navegador homologado. |
| Safari | Versão atual | Homologado para dispositivos Apple (macOS e iOS). |

Importante

O **Microsoft Edge Legacy** (versões baseadas em EdgeHTML, anteriores a 2020) foi descontinuado pela Microsoft e não é mais suportado pelo TOTVS Identity. A partir da transição para a base **Chromium**, o Microsoft Edge compartilha da mesma compatibilidade técnica do Google Chrome.

## SmartSync e Desktop SSO

---

Requisitos de *hardware* e sistema para implantação do SmartSync e Desktop SSO:

|  |  |  |
| --- | --- | --- |
| Sistema Operacional | Windows Server 2012, 2016, 2019 ou 2022 | |
| Memória RAM | 4 GB | |
| Processador | Arquitetura | 64 bits |
| Core | Mínimo 2 núcleos |
| Disco | Velocidade | 7200 RPM |
| Taxa de transferência | Mínimo 1GB/s |
| Espaço em disco | 40 GB |
| .NET Runtime | Conforme versão do instalador (veja abaixo). | |
| Rede | O servidor em que o SmartSync está instalado deve, obrigatoriamente, ser capaz de acessar os domínios do Identity (\*.fluigidentity.com e \*.customerfi.com) para que a sincronização e a autenticação dos usuários do Active Directory sejam efetuadas.  O cliente deve providenciar para que as devidas exceções sejam adicionadas ao *proxy* e *firewall* de sua rede. | |

As versões do Novo SmartSync possuem dependências específicas do runtime do .NET:

| Componente | Requisito de Software (conforme versão) |
| --- | --- |
| SmartSync (Legado) | .NET Framework 4.8 ou superior |
| Novo SmartSync | • Versões até 5.1.X.X: **.NET 6 ou superior**  • Versão 5.2.X.X: **.NET 8 ou superior**  • Versão 5.3.X.X: **.NET 10 (Planejado)** |

## Desktop Launcher e SSO Profile Generator

---

Requisitos de sistema para instalação do Desktop Launcher e Thick SSO Profile Generator:

|  |  |
| --- | --- |
| Sistema Operacional | Windows 7 ou superior |
| .NET Framework | 7.5 |

## Portas

---

* A integração do Identity com o SmartSync ocorre através da porta 5325. Mas é possível trocar a porta, para mais detalhes consulte a documentação .
* O SmartSync exige que a saída esteja liberada para [adsync.customerfi.com](http://adsync.customerfi.com/) pela porta 443 (em customerfi) e [adsync.fluigidentity.com](http://adsync.fluigidentity.com/) pela porta 443 (produção).

]]>
