---
content_hash: 15f4f050a6a1fc7b8402e6f7cae1af5640f7e1618059db02f938557fa6f8a03d
fetched_at: '2026-07-02T19:24:28.777072+00:00'
page_id: '853929494'
product: protheus
source: tdn-tec
title: CopyToDelim
type: documentation
url: https://tdn.totvs.com/display/tec/CopyToDelim
version: 2
---

BLOCK

CopyToDelim

# CopyToDelim

Se for informado muda padrão de envio das funções "" e "", e dos comandos AdvPL "**Copy to**" quando traduzidos nessas funções.

O comportamento padrão de envio destas funções é de enviar linha a linha, porém quando este parâmetro é configurado, o envio é feito em blocos que contenham minimamente o tamanho informado, ou seja, toda vez que a soma do tamanho em bytes das linhas anteriores ultrapassar este limite, o bloco e enviado e começa um novo bloco vazio.

O valor do bloco deve ser informado em bytes, todavia se for passado 0 ou menor o envio é mantido como o padrão, que é de enviar linha a linha.

```

```

### Valores válidos

| Valores | Descrição |
| --- | --- |
| maiores que 0 (zero) | Altera padrão de envio definindo um bloco do dados a ser enviado. Valor deve ser informado em bytes |
| 0 (zero) ou menores que 0 (zero) | Usa o envio padrão linha a linha |

### Exemplo

```
[General]  
# altera o envio padrao para envio em blocos. Ex: Bloco de 100 Kb  
CopyToDelim=102400
```

## Observações

* Este recurso está disponível a partir do build **20.3.2.12**, a alteração do seu valor pode aumentar o consumo de memória baseado no tamanho do bloco, assim com também interferirá na taxa de transmissão dos dados.  
  Bloco maiores tendem a ter uma taxa de transmissão maior, porém são mais suscetíveis as intempéries da rede, o tamanho do bloco deve ser avaliado na infraestrutura na qual ele está em uso, pois pode gerar falhas na transmissão.

## Veja também
