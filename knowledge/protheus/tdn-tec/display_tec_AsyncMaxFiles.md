---
content_hash: 816388bec6249a1e4591bd0f99c27a478cf3e813b5b31d8772f52f5beba8b26d
fetched_at: '2026-07-02T19:24:28.781350+00:00'
page_id: '853933055'
product: protheus
source: tdn-tec
title: AsyncMaxFiles
type: documentation
url: https://tdn.totvs.com/display/tec/AsyncMaxFiles
version: 2
---

BLOCK

AsyncMaxFiles

# AsyncMaxFiles

```
Permite alterar a quantidade máxima de arquivos de log assíncronos gravados do TOTVS | Application Server.  
Por padrão mantém os dois últimos arquivos, para utilizar você deve habilitar a gravação de logs assíncronos:   
  
Quando o número máximo de arquivos gravados é atingido, o TOTVS | Application Server começa a sobrescrever o primeiro arquivo.  
  
Quando o serviço é reiniciado, se não tiver atingido o máximo de arquivos gravados ou houver algum deles que tenha sido removido,  
este será o próximo arquivo a ser utilizado, e os próximos serão criados/sobrescritos, porém se todos os arquivos já tiverem sido   
gravados, o TOTVS | Application Server procura o mais antigo e começa a regravar sobre ele, mantendo assim os logs mais recentes.
```

### Valores válidos

| Valores | Descrição |
| --- | --- |
| 0 | Não limita a quantidade de arquivos serem gravados |
| maior ou igual a 1 | Define a quantidade de arquivos que serão mantidos. Por padrão são 2 arquivos. |
| menor que 0 | Mantém o valor padrão. |

### Exemplo

```
[General]  
AsyncConsoleLog=1  
; Passa a armazenar 7 arquivos de log  
AsyncMaxFiles=7
```

## Veja também
